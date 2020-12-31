# dehaze

## dehaze v1
对浓雾天气下拍摄，导致细节无法辨认的图像进行去雾处理，还原更清晰真实的图像。

### 请求参数

* `image_path (str)` - 如果识别图片存储在服务器可访问的本地路径时，使用该选项。默认优先使用`image_path`。
* `image_data (str)` - base64编码后的图片数据，要求编码后大小不超过4M，支持jpg/jpeg/png/bmp格式。

示例代码：
```python
import base64
import requests

vals = {"image_path": "/workspace/cicba/images/dehaze_01.jpg"}
url = "http://localhost:7003/dehaze"
response = requests.post(url, data=vals)
data = response.json()

# One
if data["status"] != "0":
    print(data)
else:
    img_data = base64.b64decode(data["data"])
    with open("/workspace/images/test_out.jpg", "wb") as f:
        f.write(img_data)

# Two
from PIL import Image
from io import BytesIO
img = Image.open(BytesIO(img_data))
```

### 返回参数

* `status (int)` - 若`status=0`，表示正常；否则，返回非零值，请求出错了。
* `data (str)` - 若`status=0`，则返回base64编码图片；否则，返回错误描述信息。

返回示例：
```
{
    "status": 0,
    "data": "????"
}
```
