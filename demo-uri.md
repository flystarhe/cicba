# Demo - python
* 内网地址：`172.18.141.232`
* 外网地址：`121.196.105.210`

```python
!ls -AlF /workspace/images/demo
```

    total 1196
    drwxr-xr-x 2 root root   4096 Jan  6 06:22 .ipynb_checkpoints/
    -rw-r--r-- 1 root root 111690 Jan  4 15:02 bankcard_01.jpg
    -rw-r--r-- 1 root root 226618 Jan  4 15:02 dehaze_01.jpg
    -rw-r--r-- 1 root root   4947 Jan  6 06:33 demo-uri.ipynb
    -rw-r--r-- 1 root root  12518 Jan  4 15:34 demo.ipynb
    -rw-r--r-- 1 root root 266694 Jan  4 15:02 detection_01.jpg
    -rw-r--r-- 1 root root 138481 Jan  4 15:02 detection_02.jpg
    -rw-r--r-- 1 root root 237236 Jan  4 15:02 detection_03.jpg
    -rw-r--r-- 1 root root 203240 Jan  4 15:02 idcard_01.jpg


## uri


```python
import requests

vals = {"image_path": "https://aip.bdstatic.com/portal-pc-node/dist/1609320349932/images/technology/vehicle/detect/1.jpg", "score_thr": 0.5, "mode": "det"}
url = "http://121.196.105.210:7005/detection"
response = requests.post(url, data=vals)
print(response.json())
```

    {'status': 0, 'data': {'bbox': [{'xyxy': [1189.452392578125, 656.8873291015625, 1269.86572265625, 705.4522705078125], 'label': 'car', 'score': 0.9974004030227661}, {'xyxy': [1364.575927734375, 715.0731201171875, 1497.0838623046875, 780.3200073242188], 'label': 'car', 'score': 0.9940137267112732}, {'xyxy': [1024.2767333984375, 582.6420288085938, 1067.1143798828125, 620.1596069335938], 'label': 'car', 'score': 0.9875046610832214}, {'xyxy': [237.01031494140625, 605.8427124023438, 569.0455322265625, 919.6438598632812], 'label': 'truck', 'score': 0.9942713975906372}]}}



```python
import requests

vals = {"image_path": "/workspace/cicba/images/detection_01.jpg", "score_thr": 0.5, "mode": "det"}
url = "http://121.196.105.210:7005/detection"
response = requests.post(url, data=vals)
print(response.json())
```

    {'status': 0, 'data': {'bbox': [{'xyxy': [1189.452392578125, 656.8873291015625, 1269.86572265625, 705.4522705078125], 'label': 'car', 'score': 0.9974004030227661}, {'xyxy': [1364.575927734375, 715.0731201171875, 1497.0838623046875, 780.3200073242188], 'label': 'car', 'score': 0.9940137267112732}, {'xyxy': [1024.2767333984375, 582.6420288085938, 1067.1143798828125, 620.1596069335938], 'label': 'car', 'score': 0.9875046610832214}, {'xyxy': [237.01031494140625, 605.8427124023438, 569.0455322265625, 919.6438598632812], 'label': 'truck', 'score': 0.9942713975906372}]}}


## bytes


```python
uri = "/workspace/cicba/images/detection_01.jpg"

import base64
with open(uri, "rb") as f:
    image_data = base64.b64encode(f.read())

vals = {"image_data": image_data, "score_thr": 0.5, "mode": "det"}
url = "http://121.196.105.210:7005/detection"
response = requests.post(url, data=vals)
print(response.json())
```

    {'status': 0, 'data': {'bbox': [{'xyxy': [1189.452392578125, 656.8873291015625, 1269.86572265625, 705.4522705078125], 'label': 'car', 'score': 0.9974004030227661}, {'xyxy': [1364.575927734375, 715.0731201171875, 1497.0838623046875, 780.3200073242188], 'label': 'car', 'score': 0.9940137267112732}, {'xyxy': [1024.2767333984375, 582.6420288085938, 1067.1143798828125, 620.1596069335938], 'label': 'car', 'score': 0.9875046610832214}, {'xyxy': [237.01031494140625, 605.8427124023438, 569.0455322265625, 919.6438598632812], 'label': 'truck', 'score': 0.9942713975906372}]}}

