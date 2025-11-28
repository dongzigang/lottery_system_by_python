#!/usr/bin/env python
# coding:utf-8
""" 
@Tíme:   2025/11/27 - 21:57
@Author: 199312306017deg@gmail.com
@File:   error.py
"""
class NotPathError(Exception):
    pass

class FormatError(Exception):
    pass

class NotFileError(Exception):
    def __init__(self, message):
        super().__init__(message)

class UserExistsError(Exception):
    def __init__(self, message):
        super().__init__(message)