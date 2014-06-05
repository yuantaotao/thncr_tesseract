#!/usr/bin/env python

'''
File: pytesser.py
Author: Dennis( yuantaotao@gmail.com )
Description: from pytesser on googlecode
'''

import Image
import subprocess

import util
import errors
import hashlib

tesseract_exe_name = 'tesseract' # Name of executable to be called at command line
scratch_text_name_root = "/tmp/%s_temp" % "tmp" # Leave out the .txt extension
scratch_image_name = scratch_text_name_root + ".bmp" # This file must be .bmp or other Tesseract-compatible format
cleanup_scratch_flag = True  # Temporary files cleaned up after OCR operation

def call_tesseract(input_filename, output_filename, learn_file='eng'):
    """Calls external tesseract.exe on input file (restrictions on types),
    outputting output_filename+'txt'"""
    #args = [tesseract_exe_name, input_filename, output_filename]
    args = [tesseract_exe_name, input_filename, output_filename, '-l', learn_file]
    devnull = open('/dev/null', 'w')
    proc = subprocess.Popen(args, stdout=devnull)
    retcode = proc.wait()
    if retcode!=0:
        pass
        #errors.check_for_errors()
    devnull.close()

def image_to_string(im, cleanup = cleanup_scratch_flag, learn_file='eng'):
    """Converts im to file, applies tesseract, and fetches resulting text.
    If cleanup=True, delete scratch files after operation."""
    scratch_text_name_root = "/tmp/%s_temp" % hashlib.md5(im.tostring()).hexdigest()
    scratch_image_name = scratch_text_name_root + ".bmp"
    try:
        util.image_to_scratch(im, scratch_image_name)
        call_tesseract(scratch_image_name, scratch_text_name_root, learn_file)
        text = util.retrieve_text(scratch_text_name_root)
    finally:
        if cleanup:
            util.perform_cleanup(scratch_image_name, scratch_text_name_root)
    return text

def image_file_to_string(filename, cleanup = cleanup_scratch_flag, graceful_errors=True):
    """Applies tesseract to filename; or, if image is incompatible and graceful_errors=True,
    converts to compatible format and then applies tesseract.  Fetches resulting text.
    If cleanup=True, delete scratch files after operation."""
    try:
        try:
            call_tesseract(filename, scratch_text_name_root)
            text = util.retrieve_text(scratch_text_name_root)
        except errors.Tesser_General_Exception:
            if graceful_errors:
                im = Image.open(filename)
                text = image_to_string(im, cleanup)
            else:
                raise
    finally:
        if cleanup:
            util.perform_cleanup(scratch_image_name, scratch_text_name_root)
    return text


if __name__=='__main__':
    im = Image.open('phototest.tif')
    text = image_to_string(im)
    print text
    try:
        text = image_file_to_string('fnord.tif', graceful_errors=False)
    except errors.Tesser_General_Exception, value:
        print "fnord.tif is incompatible filetype.  Try graceful_errors=True"
        print value
    text = image_file_to_string('fnord.tif', graceful_errors=True)
    print "fnord.tif contents:", text
    text = image_file_to_string('fonts_test.png', graceful_errors=True)
    print text


