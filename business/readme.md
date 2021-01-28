# business

## business v1
可结构化识别各类版式的营业执照，返回证件编号、社会信用代码、单位名称、地址、法人、类型、成立日期、有效日期、经营范围等关键字段信息。

### 请求参数

* `image (str)` - 服务器可访问的本地路径或URL
* `accuracy (str)` - `normal`使用快速服务，`high`使用高精度服务

示例代码：
```python
import requests

vals = {"image": "/workspace/cicba/images/business_01.png", "accuracy": "high"}
url = "http://localhost:7007/business"
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
        "社会信用代码": {
            "words": "10440119MA06M8503",
            "location": {
                "top": 296,
                "left": 237,
                "width": 178,
                "height": 18
            }
        },
        "组成形式": {
            "words": "无",
            "location": {
                "top": -1,
                "left": -1,
                "width": 0,
                "height": 0
            }
        },
        "经营范围": {
            "words": "商务服务业",
            "location": {
                "top": 587,
                "left": 378,
                "width": 91,
                "height": 18
            }
        },
        "成立日期": {
            "words": "2019年01月01日",
            "location": {
                "top": 482,
                "left": 1045,
                "width": 119,
                "height": 19
            }
        },
        "法人": {
            "words": "方平",
            "location": {
                "top": 534,
                "left": 377,
                "width": 39,
                "height": 19
            }
        },
        "注册资本": {
            "words": "200万元",
            "location": {
                "top": 429,
                "left": 1043,
                "width": 150,
                "height": 19
            }
        },
        "证件编号": {
            "words": "921MA190538210301",
            "location": {
                "top": 216,
                "left": 298,
                "width": 146,
                "height": 16
            }
        },
        "地址": {
            "words": "广州市",
            "location": {
                "top": 585,
                "left": 1041,
                "width": 55,
                "height": 19
            }
        },
        "单位名称": {
            "words": "有限公司",
            "location": {
                "top": 429,
                "left": 382,
                "width": 72,
                "height": 19
            }
        },
        "有效期": {
            "words": "长期",
            "location": {
                "top": 534,
                "left": 1045,
                "width": 0,
                "height": 0
            }
        },
        "类型": {
            "words": "有限责任公司(自然人投资或控股)",
            "location": {
                "top": 482,
                "left": 382,
                "width": 260,
                "height": 18
            }
        }
    }
}
```
