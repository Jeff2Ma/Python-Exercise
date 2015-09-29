#!/usr/bin/python
# -*- coding: utf-8 -*-

# by JeffMa at http://devework.com/

# 题目：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random
import os
import string


def GenKey(length):
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars) for i in range(length)])


def SaveKey(content):
    f = open('Result Key.txt', 'a')
    f.write(content)
    f.write('\n')
    f.close()


if __name__ == '__main__':
    for i in range(20):
        value = GenKey(20)
        print value
        SaveKey(value)
