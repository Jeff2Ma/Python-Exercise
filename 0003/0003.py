#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
"""
import redis, random, string

r = redis.Redis(host='localhost', port=6379)

def GenKey(length):
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars) for i in range(length)])

if __name__ == '__main__':
    for i in range(200):
        value = GenKey(20)
        r.set(i,value)
        print i,':',r.get(i)