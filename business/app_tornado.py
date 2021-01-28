import base64
import re
import requests
import sys
import tornado.ioloop
import tornado.web
import traceback
from business.utils import for_image_data
from business.utils import for_image_path


URL_REGEX = re.compile(r"http://|https://|ftp://")


def imread(uri):
    if URL_REGEX.match(uri):
        return base64.b64encode(requests.get(uri).content)
    with open(uri, "rb") as f:
        return base64.b64encode(f.read())


G_AK = "doMFkEYsD3eVKi2O8QuyiPlH"
G_SK = "wPQAue6Be36Ww6fk9mY6fAFygsdmgl4p"


class BusinessHandler(tornado.web.RequestHandler):

    def post(self):
        global G_AK, G_SK
        try:
            params = self.request.body_arguments
            err_str = "Missing argument: " + ",".join(params.keys())
            assert "image" in params and "accuracy" in params, err_str

            image_path = params["image"][-1].decode("utf-8")
            image_data = imread(image_path)

            accuracy = params["accuracy"][-1].decode("utf-8")
            code, data = for_image_data(image_data, accuracy, G_AK, G_SK)

            res = {"status": code, "data": data}
        except Exception:
            err = traceback.format_exc()
            res = {"status": 1, "data": err}
        self.finish(res)


def make_app():
    return tornado.web.Application([
        (r"/business", BusinessHandler),
    ])


if __name__ == "__main__":
    if len(sys.argv) > 3:
        G_AK, G_SK = sys.argv[2], sys.argv[3]
    print("AK: {}\nSK: {}\n".format(G_AK, G_SK))

    app = make_app()
    app.listen(sys.argv[1])
    tornado.ioloop.IOLoop.current().start()
