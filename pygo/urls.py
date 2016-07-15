# coding:utf-8
import os
import tornado.web

from views.main import MainHandler
from common.tools import make_mongo
from config import DEBUG

mongodb = make_mongo()

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "mongodb": mongodb
}


def make_app():
    app = tornado.web.Application(
        [
            (r"/index", MainHandler),
        ], debug=DEBUG, **settings)
    # print settings
    return app
