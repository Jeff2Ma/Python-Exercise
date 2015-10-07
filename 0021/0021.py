#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://pythoncentral.io/hashing-strings-with-python/
"""
第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

阅读资料 用户密码的存储与 Python 示例

阅读资料 Hashing Strings with Python

阅读资料 Python's safest method to store and retrieve passwords from a database
"""

import uuid
import hashlib

def hash_password(password):
    # uuid 用以产生随机的盐值
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = raw_input('请输入待加密的密码: ')
hashed_password = hash_password(new_pass)
print('加密后: ' + hashed_password)
old_pass = raw_input('请输入密码以供检测:')
if check_password(hashed_password, old_pass):
    print('密码正确!')
else:
    print('密码不正确!')