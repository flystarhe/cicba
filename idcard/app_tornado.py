import sys
import tornado.ioloop
import tornado.web
import traceback
from idcard.utils import for_image_data
from idcard.utils import for_image_path


G_AK = "doMFkEYsD3eVKi2O8QuyiPlH"
G_SK = "wPQAue6Be36Ww6fk9mY6fAFygsdmgl4p"


class IdCardHandler(tornado.web.RequestHandler):

    def post(self):
        global G_AK, G_SK
        try:
            params = self.request.body_arguments
            err_str = "Missing argument: " + ",".join(params.keys())
            assert "image_path" in params or "image_data" in params, err_str
            assert "card_side" in params, err_str

            if "image_path" in params:
                image_path = params["image_path"][-1].decode("utf-8")
                card_side = params["card_side"][-1].decode("utf-8")
                code, data = for_image_path(image_path, card_side, G_AK, G_SK)
            else:
                image_data = params["image_data"][-1]
                card_side = params["card_side"][-1].decode("utf-8")
                code, data = for_image_data(image_data, card_side, G_AK, G_SK)

            res = {"status": code, "data": data}
        except Exception:
            err = traceback.format_exc()
            res = {"status": 1, "data": err}
        self.finish(res)


def make_app():
    return tornado.web.Application([
        (r"/idcard", IdCardHandler),
    ])


if __name__ == "__main__":
    if len(sys.argv) > 3:
        G_AK, G_SK = sys.argv[2], sys.argv[3]
    print("AK: {}\nSK: {}\n".format(G_AK, G_SK))

    app = make_app()
    app.listen(sys.argv[1])
    tornado.ioloop.IOLoop.current().start()
