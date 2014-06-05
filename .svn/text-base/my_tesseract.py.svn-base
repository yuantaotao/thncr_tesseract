#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
使用tesserwrap识别图片验证码的模块

项目主页见 https://github.com/gregjurman/tesserwrap
"""
import Image
import StringIO
import re
import urllib2

from tesserwrap import tesseract


class ImageRecer(object):
    """用于图片识别的类
    """

    def __init__(self):
        self.tw = tesseract('./', 'dod')

    def study(self, site=''):
        """兼容旧接口
        """
        pass

    def recog(self, template, data, expected=""):
        """传入图片内容并识别

        :param data: 传入的图片内容
        :return: 识别出的字符串
        """
        try:
            data_to_file = StringIO.StringIO(data)
        except:
            print "not valid image? %s" % data
            return ""
        if template == "360":
            learn_file = 'dod'
        else:
            learn_file = 'eng'
        img = Image.open(data_to_file)
        price = self.tw.ocr_image(img)
        price = re.sub(r'\n', '', price)
        price = re.sub(r' ', '', price)
        if re.match(r'^Y[1-9][0-9]*\.[0-9]{2}$', price):
            return (price, '', 1.0)


if __name__ == "__main__":

    tester = ImageRecer()
    url1 = 'http://price.360buyimg.com/gp548609,3.png'
    data = urllib2.urlopen(url1).read()
    print tester.recog('360', data)
    url2 = 'http://price.360buyimg.com/gp656205,3.png'
    data = urllib2.urlopen(url2).read()
    print tester.recog('360', data)
