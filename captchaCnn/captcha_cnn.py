import os

import tensorflow as tf
from PIL import Image
import numpy as np

from captchaCnn.cnn_train import cnn_graph
from captchaCnn.captcha_gen import gen_captcha_text_and_image
from captchaCnn.util import vec2text, convert2gray
from captchaCnn.util import CAPTCHA_LIST, CAPTCHA_WIDTH, CAPTCHA_HEIGHT, CAPTCHA_LEN

x = tf.placeholder(tf.float32, [None, CAPTCHA_HEIGHT * CAPTCHA_WIDTH])
keep_prob = tf.placeholder(tf.float32)
y_conv = cnn_graph(x, keep_prob, (CAPTCHA_HEIGHT, CAPTCHA_WIDTH))
saver = tf.train.Saver()

def captcha2text(image_list, height=CAPTCHA_HEIGHT, width=CAPTCHA_WIDTH):
    '''
    验证码图片转化为文本
    :param image_list:
    :param height:
    :param width:
    :return:
    '''

    # print('================   ', tf.train.latest_checkpoint('D:\\pythonworkspace\\cmcc\\captchaCnn'))
    with tf.Session() as sess:
        saver.restore(sess, tf.train.latest_checkpoint('D:\\pythonworkspace\\cmcc\\captchaCnn'))
        predict = tf.argmax(tf.reshape(y_conv, [-1, CAPTCHA_LEN, len(CAPTCHA_LIST)]), 2)
        vector_list = sess.run(predict, feed_dict={x: image_list, keep_prob: 1})
        vector_list = vector_list.tolist()
        text_list = [vec2text(vector) for vector in vector_list]
        return text_list


def pre_test(path=None):
    d = {}
    for root, dirs, files in os.walk(path):
        for n in files:
            filepath = root + os.sep + n
            image = Image.open(filepath)
            captcha_image = np.array(image.getdata()).reshape(CAPTCHA_HEIGHT, CAPTCHA_WIDTH, -1)
            name = n.replace('.png', '')
            d[name] = captcha_image
    return d


if __name__ == '__main__':
    d = pre_test(path='E:\\processpic\\pretest')

    for k, v in d.items():
        image = v.flatten() / 255
        pre_text = captcha2text([image])
        print('Label:', k, ' Predict:', pre_text)
