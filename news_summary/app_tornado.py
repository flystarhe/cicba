import sys
import tornado.ioloop
import tornado.web
import traceback
from news_summary.utils import nlp_news_summary


G_AK = "9zXDM42tKyYzmOEdIDhO306A"
G_SK = "dG6RWePPFzGHq4YUYjQtS7U4xV95H3rG"


class NewsSummaryHandler(tornado.web.RequestHandler):

    def post(self):
        global G_AK, G_SK
        try:
            params = self.request.body_arguments
            err_str = "Missing argument: " + ",".join(params.keys())
            assert "title" in params and "content" in params and "max_summary_len" in params, err_str

            title = params["title"][-1].decode("utf-8")
            content = params["content"][-1].decode("utf-8")
            max_summary_len = params["max_summary_len"][-1].decode("utf-8")
            code, data = nlp_news_summary(title, content, int(max_summary_len), G_AK, G_SK)
            res = {"status": code, "data": data}
        except Exception:
            err = traceback.format_exc()
            res = {"status": 1, "data": err}
        self.finish(res)


def make_app():
    return tornado.web.Application([
        (r"/news_summary", NewsSummaryHandler),
    ])


if __name__ == "__main__":
    if len(sys.argv) > 3:
        G_AK, G_SK = sys.argv[2], sys.argv[3]
    print("AK: {}\nSK: {}\n".format(G_AK, G_SK))

    app = make_app()
    app.listen(sys.argv[1])
    tornado.ioloop.IOLoop.current().start()
