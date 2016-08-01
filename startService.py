# -*- coding: utf-8 -*-
# @Time    : 16/7/31 下午10:58
# @Author  : liulei
# @Brief   : 
# @File    : startService.py
# @Software: PyCharm Community Edition

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.httpclient
import tornado.netutil
from tornado.options import define, options
import sys


class TfTest(tornado.web.RequestHandler):
    def get(self):
        self.write("tf test!")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/tf/test", TfTest)
        ]
        settings = {}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    port = sys.argv[1]
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()