import tornado.httpserver
from tornado.options import options

from config import APP_ADDR,APP_PORT
from urls import make_app

app = make_app()

options.parse_command_line()


app.listen(APP_PORT, address=APP_ADDR)
io_loop = tornado.ioloop.IOLoop.instance()
tornado.ioloop.IOLoop.instance().start()
