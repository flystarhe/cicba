import base64
import requests
import time


G_TOKEN = "none"
G_TOKEN_LIMIT = time.time()


def _get_token(ak, sk):
    global G_TOKEN, G_TOKEN_LIMIT

    request_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"
    request_url = "{}&client_id={}&client_secret={}".format(request_url, ak, sk)

    try:
        response = requests.get(request_url)

        data = response.json()
        G_TOKEN = data["access_token"]
        G_TOKEN_LIMIT = time.time() + data["expires_in"] - 600

        return True
    except Exception as e:
        print(time.strftime("%m/%d %H:%M"), "_get_token()", e)
        return False


def get_token(ak, sk):
    global G_TOKEN, G_TOKEN_LIMIT

    if time.time() > G_TOKEN_LIMIT:
        for i in range(3):
            print(time.strftime("%m/%d %H:%M"), "_get_token()", i)
            if _get_token(ak, sk):
                break

    return G_TOKEN


def get_request_url(ak, sk):
    return "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard?access_token=" + get_token(ak, sk)


def for_image_data(img_data, card_side, ak, sk):
    try:
        request_url = get_request_url(ak, sk)
        params = {"image": img_data, "id_card_side": card_side}
        headers = {"content-type": "application/x-www-form-urlencoded"}
        response = requests.post(request_url, data=params, headers=headers)
        data = response.json()

        if "image_status" in data:
            status = data["image_status"]
            if status == "normal":
                return 0, data["words_result"]
            if status == "reversed_side":
                return 1, "身份证正反面颠倒"
            if status == "non_idcard":
                return 1, "上传的图片中不包含身份证"
            if status == "blurred":
                return 1, "身份证模糊"
            if status == "other_type_card":
                return 1, "其他类型证照"
            if status == "over_exposure":
                return 1, "身份证关键字段反光或过曝"
            if status == "over_dark":
                return 1, "亮度过低"
            return 1, "unknown"
        return 1, data["error_msg"]
    except Exception as e:
        return 1, str(e)


def for_image_path(img_path, card_side, ak, sk):
    try:
        with open(img_path, "rb") as f:
            img_data = base64.b64encode(f.read())
        return for_image_data(img_data, card_side, ak, sk)
    except Exception as e:
        return 1, str(e)
