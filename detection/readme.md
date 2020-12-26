# detection

## detection + segmentation
支持COCO目标检测任务的80个对象类别。使用模型为精度与速度折中的`X-101-32x4d-FPN`。

```
names: ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
        'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
        'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
        'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
        'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
        'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
        'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
        'hair drier', 'toothbrush']
```

### 请求参数

* `image_path (str)` - 如果识别图片存储在服务器可访问的本地路径时，使用该选项。默认优先使用`image_path`。
* `image_data (str)` - base64编码后的图片数据，要求编码后大小不超过4M，支持jpg/jpeg/png/bmp格式。
* `score_thr (float)` - 取值范围为`[0., 1.]`，置信度低于`score_thr`的检测结果会被忽略，
* `mode (str)` - `det`表示执行目标检测任务，`seg`表示执行实例分割任务。

示例代码：
```python
import requests

vals = {"image_path": "test.png", "score_thr": 0.3, "mode": "seg"}
url = "http://localhost:7005/detection"
response = requests.post(url, data=vals)
print(response.json())
```

### 返回参数

* `status (int)` - 若`status=0`，表示正常；否则，返回非零值，请求出错了。
* `data (str or dict)` - 若`status=0`，则返回结果字典；否则，返回错误描述信息。

当`mode=det`时：
```
{
    "status": 0,
    "data": 
    {
        "bbox": 
        [
            {"xyxy": [100, 200, 200, 400], "label": "car", "socre": 0.9},
            ...
        ]
    }
}
```

当`mode=seg`时：
```
{
    "status": 0,
    "data":
    {
        "bbox":
        [
            {"xyxy": [100, 200, 200, 400], "label": "car", "socre": 0.9},
            ...
        ],
        "mask":
        [
            [[[19, 32], [19, 138], [200, 138], [200, 32]], ...],  # contours, contour is [[x, y], [x, y], ...]
            ...
        ]
    }
}
```
