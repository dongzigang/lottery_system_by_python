#!/usr/bin/env python
# coding:utf-8
""" 
@Tíme:   2025/11/27 - 21:36
@Author: 199312306017deg@gmail.com
@File:   base.py
"""
import time
import json
import os
from common import utils, error

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


    def __read_user(self, time2str=False):
        with open(self.user_json, 'r') as f:
            data = json.loads(f.read())
            if time2str:
                for k, v in data.items():
                    v['create_time'] = utils.timestamp2string(v['create_time'])
                    v['update_time'] = utils.timestamp2string(v['update_time'])
                    data[k] = v
        return  data


    def __write__user(self, **user):
        if 'username' not in user:
            raise ValueError('messing username')
        if 'role' not in user:
            raise ValueError('messing role')
        user['active'] = True
        user['create_time'] = time.time()
        user['update_time'] = time.time()
        user['gifts'] = []

        users = self.__read_user()
        if user['username'] in users:
            raise error.UserExistsError('username %s has exists' % user['username'])

        users.update(
            {users['username']: user}
        )
        json_user = json.dumps(users)
        with open(self.user_json, 'w') as f:
            f.write(json_user)


if __name__ == '__main__':
    current_path = os.getcwd()
    user_json_path = os.path.join(current_path, 'storage','user.json')
    gift_json_path = os.path.join(current_path, 'storage', 'gift.json')
    base = Base(user_json= user_json_path, gift_json= gift_json_path)

