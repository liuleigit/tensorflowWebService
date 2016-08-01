# -*- coding: utf-8 -*-
# @Time    : 16/8/1 下午4:33
# @Author  : liulei
# @Brief   : tensorflow actions
# @File    : tf_api.py.py
# @Software: PyCharm Community Edition

import os
import tensorflow as tf
import tensorflow.models.embedding.word2vec_optimized as w2v

def getWord2VecModle(session):
    train_data = 'tex8'
    eval_data = 'questions-words.txt'
    save_path = '/tmp'
    opts = w2v.Options()
    opts.train_data = train_data
    opts.eval_data = eval_data
    opts.save_path = save_path
    #with tf.Graph().as_default(), tf.Session() as session:
        #with tf.device("/cpu:0"):
    with tf.device("/cpu:0"):
        model = w2v.Word2Vec(opts, session)
    for _ in xrange(opts.epochs_to_train):
        model.train()  # Process one epoch
        model.eval()  # Eval analogies.
    # Perform a final save.
    model.saver.save(session, os.path.join(opts.save_path, "model.ckpt"),
                     global_step=model.step)
    print '-----model finished--------'
    print model.analogy('king', 'man', 'queen')
    return model

def getNextWord(model, word1, word2, word3):
    return model.analogy(word1, word2, word3)