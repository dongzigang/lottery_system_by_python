#!/usr/bin/env python
# coding:utf-8
""" 
@Tíme:   2025/11/27 - 21:36
@Author: 199312306017deg@gmail.com
@File:   base.py
"""
import os
from common import utils
class Base(object):
    def __init__(self, user_json, gift_json):
        self.user_json = user_json
        self.gift_json = gift_json

        self.__check_user_json()
        self.__check_gift_json()

    def __check_user_json(self):
        utils.check_file(self.user_json)

    def __check_gift_json(self):
        utils.check_file(self.gift_json)

if __name__ == '__main__':
    current_path = os.getcwd()
    user_json_path = os.path.join(current_path, 'storage','user.json')
    gift_json_path = os.path.join(current_path, 'storage', 'gift.json')
    base = Base(user_json= user_json_path, gift_json= gift_json_path)

