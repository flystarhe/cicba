import cv2 as cv
import numpy as np
import os
from pathlib import Path


"""
        "bbox":
        [
            {"xyxy": [100, 200, 200, 400], "label": "car", "score": 0.9},
            ...
        ],
        "mask":
        [
            [[[19, 32], [19, 138], [200, 138], [200, 32]], ...],  # contours, contour is [[x, y], [x, y], ...]
            ...
        ]
"""


def draw_bbox(bbox_result, img):
    for bbox in bbox_result:
        x1, y1, x2, y2 = map(int, bbox["xyxy"])
        cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0))
        cv.putText(img, "{}:{:.2f}".format(bbox["label"], bbox["score"]),
                   (x1, y1), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0))


def draw_polylines(mask_result, img):
    for mask in mask_result:
        for points in mask:
            pts = np.array(points, np.int32)
            cv.polylines(img, pts, True, (255, 0, 0))


def image_show(out_dir, img, bbox_result, mask_result):
    if isinstance(img, str):
        img = cv.imread(img, 1)
    os.makedirs(out_dir, exist_ok=True)

    draw_bbox(bbox_result, img)
    if mask_result is not None:
        draw_polylines(mask_result, img)
    cv.imwrite(os.path.join(out_dir, "out.png"), img)
