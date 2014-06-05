"""Utility functions for processing images for delivery to Tesseract"""

import os

def image_to_scratch(im, scratch_image_name):
    """Saves image in memory to scratch file.  .bmp format will be read correctly by Tesseract"""
    im.save(scratch_image_name, dpi=(200,200))

def retrieve_text(scratch_text_name_root):
    text = ''
    try:
        inf = file(scratch_text_name_root + '.txt')
        text = inf.read()
        inf.close()
    except Exception:
        pass
    return text

def perform_cleanup(scratch_image_name, scratch_text_name_root):
    """Clean up temporary files from disk"""
    #for name in (scratch_image_name, scratch_text_name_root + '.txt', "tesseract.log"):
    for name in (scratch_image_name, scratch_text_name_root + '.txt'):
        try:
            os.remove(name)
        except Exception:
            pass
