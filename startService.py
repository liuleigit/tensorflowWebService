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
import tensorflow as tf
#import tensorflow.models.embedding.word2vec_optimized as w2v
import tf_api

model = 0

class TfTest(tornado.web.RequestHandler):
    def get(self):
        self.write("tf test!")

class WordEmbeding(tornado.web.RequestHandler):
    def get(self):
        w1 = self.get_arguments('word1', None)
        w2 = self.get_arguments('word2', None)
        w3 = self.get_arguments('word3', None)
        w4 = tf_api.getNextWord(w1, w2, w3)
        self.write(w4)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/tf/test", TfTest),
            (r"/tf/w2v", WordEmbeding)
        ]
        settings = {}
        tornado.web.Application.__init__(self, handlers, **settings)



session = tf.Session()

if __name__ == "__main__":
    port = sys.argv[1]
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())

    model = tf_api.getWord2VecModle(session)

    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()