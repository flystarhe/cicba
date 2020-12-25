# bankcard

## bankcard v1
支持对主流银行卡的卡号、有效期、发卡行、卡片类型4个关键字段进行结构化识别，识别准确率超过99%。

### 请求参数

* `image_path (str)` - 如果识别图片存储在服务器可访问的本地路径时，使用该选项。默认优先使用`image_path`。
* `image_data (str)` - base64编码后的图片数据，要求编码后大小不超过4M，支持jpg/jpeg/png/bmp格式。

示例代码：
```python
import requests

vals = {"image_path": "test.png"}
url = "http://localhost:7001/bankcard"
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
    "data": {
        "valid_date": "02/12",
        "bank_card_number": "6222 3700 3333 6266",
        "bank_name": "工商银行",
        "bank_card_type": 2
    }
}
```

* `valid_date (str)` - 有效期
* `bank_card_number (str)` - 银行卡卡号
* `bank_name (str)` - 银行名，不能识别时为空
* `bank_card_type (int)`
  - 0:不能识别
  - 1:借记卡
  - 2:贷记卡（原信用卡大部分为贷记卡）
  - 3:准贷记卡
  - 4:预付费卡
