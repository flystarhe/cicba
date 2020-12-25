import sys
import tornado.ioloop
import tornado.web
import traceback
from bankcard.utils import for_image_data
from bankcard.utils import for_image_path


G_AK = "doMFkEYsD3eVKi2O8QuyiPlH"
G_SK = "wPQAue6Be36Ww6fk9mY6fAFygsdmgl4p"


class BankCardHandler(tornado.web.RequestHandler):

    def post(self):
        global G_AK, G_SK
        try:
            params = self.request.body_arguments
            if "image_path" in params:
                image_path = params["image_path"][-1].decode("utf-8")
                code, data = for_image_path(image_path, "true", G_AK, G_SK)
            elif "image_data" in params:
                image_data = params["image_data"][-1]
                code, data = for_image_data(image_data, "true", G_AK, G_SK)
            else:
                code, data = 1, "Missing argument: " + ",".join(params.keys())
            res = {"status": code, "data": data}
        except Exception:
            err = traceback.format_exc()
            res = {"status": 1, "data": err}
        self.finish(res)


def make_app():
    return tornado.web.Application([
        (r"/bankcard", BankCardHandler),
    ])


if __name__ == "__main__":
    if len(sys.argv) > 3:
        G_AK, G_SK = sys.argv[2], sys.argv[3]
    print("AK: {}\nSK: {}\n".format(G_AK, G_SK))

    app = make_app()
    app.listen(sys.argv[1])
    tornado.ioloop.IOLoop.current().start()
