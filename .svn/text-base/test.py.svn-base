#!/usr/bin/python
# -*- coding:UTF-8 -*-

import timeit

import_stmt = """\
import Image

from recog_tesseract import ImageRecer
from my_tesseract import ImageRecer as MyImageRecer
from tesserwrap import tesseract
#url = 'http://jprice.360buyimg.com/price/gp707044-1-1-3.png'
data = open('test.png').read()
"""

if __name__ == '__main__':
    t1 = timeit.Timer("tester=ImageRecer();tester.recog('360', data)",
            import_stmt)
    print 'recog_tesseract: %.3f' % t1.timeit(1000)
    t2 = timeit.Timer("tester=MyImageRecer();tester.recog('360', data)",
            import_stmt)
    print 'my_tesseract: %.3f' % t2.timeit(1000)
