#!/usr/bin/env python
# coding:utf-8
""" 
@Tíme:   2025/11/27 - 21:54
@Author: 199312306017deg@gmail.com
@File:   utils.py
"""
import os
import time
from common import error
def check_file(path):
    if not os.path.exists(path):
        raise error.NotPathError('not find %s' % path)
    if not path.endswith('.json'):
        raise error.FormatError('%s is not a json file' % path)
    if not os.path.isfile(path):
        raise error.NotFileError('%s is not a file' % path)


def timestamp2string(timestamp):
    time_obj = time.localtime(timestamp)
    time_str = time.strftime('%Y-%m-%d %H:%M:%S')
    return  time_str
