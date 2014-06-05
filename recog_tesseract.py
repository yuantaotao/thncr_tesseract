#!/usr/bin/env python

#def img_to_text(filename):
#    img = Image.open(filename)
#    img.load()
#    #if len(img.split()) == 4:
#    #    r, g, b, a = img.split()
#    #    img = Image.merge("RGB", (r, g, b))
#    #img.save("example.bmp", "BMP")
#    return image_to_string(img, False, 'jd')
#
#if __name__ == '__main__':
#    print img_to_text('/data/www/misc/upload_files/tmp/Y1349.00.png')
#



#!/usr/bin/env python

import os
import sys
import Image
import StringIO
import re
import urllib2

from pytesser import *

class ImageRecer(object):

    def __init__(self):
        pass

    def study(self, site=''):
        pass

    def recog(self, template, data, expected=""):
        try:
            data_to_file = StringIO.StringIO(data)
        except:
            print "not valid image? %s"%data
            return ""
        if template == "360":
            learn_file = 'dod'
        else:
            learn_file = 'eng'
        img = Image.open(data_to_file)
        img.load()
        if len(img.split()) == 4:
            r, g, b, a = img.split()
            #re-organize the bands of this img for giving out a img fit for orc
            img = Image.merge("RGB", (b, g, b))
            #print 'splited'
        #img.save("example.bmp", "BMP")
        price = image_to_string(img, True, learn_file)
        #print price
        #there is two \n in the output of tesseract
        price = re.sub(r'\n', '', price)
        #some times there will be spaces in the output
        price = re.sub(r' ', '', price)
        if re.match(r'^Y[1-9][0-9]*\.[0-9]{2}$', price):
            return (price, '', 1.0)
        else:
            #print "back up"
            sys.path.append('/'.join(os.getcwd().split('/')[:-1]))
            from recog import recog
            #from recog import recog
            #import recog
            bak_reader  = recog.ImageRecer()
            bak_reader.study(os.getcwd() + '/recog/data/')
            return bak_reader.recog('360', data)


if __name__=="__main__":

    sys.path.append('/'.join(os.getcwd().split('/')[:-2]))
    from commontools import tools
    tester = ImageRecer()

    #url = 'http://price.360buyimg.com/gp183224,3.png'
    url = 'http://price.360buyimg.com/gp548609,3.png'
    #data = urllib2.urlopen(url).read()
    #print len(data)
    #outfile = open('/data/www/misc/upload_files/tmp/urllib2.png','w')
    #outfile.write(data)
    #print tester.recog('360',data)

    page_getter = tools.PageGetter('', None)
    gotpage, is404, pagecontent = page_getter.get(3, url, 3)
    outfile = open('/data/www/misc/upload_files/tmp/getter.png','w')
    outfile.write(pagecontent)

    print gotpage
    print is404
    print len(pagecontent)
    print tester.recog('360',pagecontent)
