#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/

"""
第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

"""
# 引入正则表达式等模块
import re, os
from collections import Counter

def Find_frequent(file_name):
    # 匹配单词字符,然后转成小写
    words = re.findall(r'\w+', open(file_name).read().lower())
    # 找出频率最高的词汇
    print Counter(words).most_common(1)

# 遍历某个路径下所有文件
def Show_files(root_dir):
    list_dirs = os.walk(root_dir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            print os.path.join(root, d)
        for f in files:
            print os.path.join(root, f)

"""

以下是两个函数的结合

"""
def Find_frequent_word(file_name):
    # 匹配单词字符,然后转成小写
    words = re.findall(r'\w+', open(file_name).read().lower())
    # 找出频率最高的词汇
    result = Counter(words).most_common(1)
    print "文件 %s 上最重要的词汇(词汇:出现次数) %s" % (file_name, result)

def Find_frequent_in_each_file(root_dir):
    list_dirs = os.walk(root_dir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            file_name =  os.path.join(root, d)
            Find_frequent_word(file_name)
        for f in files:
            file_name = os.path.join(root, f)
            Find_frequent_word(file_name)

if __name__ == '__main__':
    Find_frequent_in_each_file("./daily")