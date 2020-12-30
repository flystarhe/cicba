import base64
import cv2 as cv
import mmcv
import numpy as np
import os
import sys
import torch
import tornado.ioloop
import tornado.web
import traceback
from io import BytesIO
from mmdet.apis import init_detector, inference_detector


os.environ["MKL_THREADING_LAYER"] = "GNU"
config_file = "/workspace/cicba/detection/mask_rcnn_x101_32x4d_fpn_2x_coco.py"
checkpoint_file = "/workspace/cicba/detection/mask_rcnn_x101_32x4d_fpn_2x_coco.pth"
model = init_detector(config_file, checkpoint_file, device="cuda:0")
names = ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light",
         "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
         "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee",
         "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
         "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
         "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch",
         "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone",
         "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
         "hair drier", "toothbrush"]


class MainHandler(tornado.web.RequestHandler):

    def post(self):
        try:
            global model, names

            params = self.request.body_arguments
            err_str = "Missing argument: " + ",".join(params.keys())
            assert "image_path" in params or "image_data" in params, err_str
            assert "score_thr" in params and "mode" in params, err_str

            if "image_path" in params:
                image_path = params["image_path"][-1].decode("utf-8")
                image_data = mmcv.imread(image_path)
            else:
                image_data = params["image_data"][-1]
                image_data = base64.b64decode(image_data)
                image_data = mmcv.imread(BytesIO(image_data))

            score_thr = params["score_thr"][-1].decode("utf-8")
            mode = params["mode"][-1].decode("utf-8")
            score_thr = float(score_thr)

            result = inference_detector(model, image_data)
            if isinstance(result, tuple):
                bbox_result, segm_result = result
            else:
                bbox_result, segm_result = result, None

            bboxes = np.vstack(bbox_result)
            labels = [
                np.full(bbox.shape[0], i, dtype=np.int32)
                for i, bbox in enumerate(bbox_result)
            ]
            labels = np.concatenate(labels)

            inds = np.where(bboxes[:, -1] > score_thr)[0]
            bboxes, labels = bboxes[inds].tolist(), labels[inds].tolist()

            bbox_result = [
                dict(xyxy=[x1, y1, x2, y2], label=names[label], score=s)
                for (x1, y1, x2, y2, s), label in enumerate(bboxes, labels)
            ]

            if "seg" == mode and segm_result is not None:
                segms = mmcv.concat_list(segm_result)
                mask_result = []
                for i in inds:
                    sg = segms[i]
                    if isinstance(sg, torch.Tensor):
                        sg = sg.detach().cpu().numpy()
                    contours = cv.findContours(sg.astype("uint8"), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[0]
                    contours = [x.squeeze().tolist() for x in contours]
                    mask_result.append(contours)
                data = {"bbox": bbox_result, "mask": mask_result}
            else:
                data = {"bbox": bbox_result}

            res = {"status": 0, "data": data}
        except Exception:
            err = traceback.format_exc()
            res = {"status": 1, "data": err}
        self.finish(res)


def make_app():
    return tornado.web.Application([
        (r"/detection", MainHandler),
        (r"/segmentation", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(sys.argv[1])
    tornado.ioloop.IOLoop.current().start()
