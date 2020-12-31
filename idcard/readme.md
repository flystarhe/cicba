# idcard

## idcard v1
支持对二代居民身份证正反面所有8个字段进行结构化识别，包括姓名、性别、民族、出生日期、住址、身份证号、签发机关、有效期限，识别准确率超过99%。

同时，支持对用户上传的身份证图片进行图像风险和质量检测，可识别图片是否为复印件或临时身份证，是否被翻拍或编辑，是否存在正反颠倒、模糊、欠曝、过曝等质量问题。

### 请求参数

* `image_path (str)` - 如果识别图片存储在服务器可访问的本地路径时，使用该选项。默认优先使用`image_path`。
* `image_data (str)` - base64编码后的图片数据，要求编码后大小不超过4M，支持jpg/jpeg/png/bmp格式。
* `card_side (str)` - `front`身份证含照片的一面，`back`身份证带国徽的一面。

示例代码：
```python
import requests

vals = {"image_path": "/workspace/cicba/images/idcard_01.jpg", "card_side": "front"}
url = "http://localhost:7002/idcard"
response = requests.post(url, data=vals)
print(response.json())
```

### 返回参数

* `status (int)` - 若`status=0`，表示正常；否则，返回非零值，请求出错了。
* `data (str or dict)` - 若`status=0`，则返回结果字典；否则，返回错误描述信息。

返回示例：
```
{
    "status": 0,
    "data":  {
        "住址": {
            "location": {
                "left": 267,
                "top": 453,
                "width": 459,
                "height": 99
            },
            "words": "南京市江宁区弘景大道3889号"
        },
        "公民身份号码": {
            "location": {
                "left": 443,
                "top": 681,
                "width": 589,
                "height": 45
            },
            "words": "330881199904173914"
        },
        "出生": {
            "location": {
                "left": 270,
                "top": 355,
                "width": 357,
                "height": 45
            },
            "words": "19990417"
        },
        "姓名": {
            "location": {
                "left": 267,
                "top": 176,
                "width": 152,
                "height": 50
            },
            "words": "伍云龙"
        },
        "性别": {
            "location": {
                "left": 269,
                "top": 262,
                "width": 33,
                "height": 52
            },
            "words": "男"
        },
        "民族": {
            "location": {
                "left": 492,
                "top": 279,
                "width": 30,
                "height": 37
            },
            "words": "汉"
        }
    }
}
```
