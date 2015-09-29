#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/

# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

from collections import Counter
text = open("short.txt").read()
counts = Counter([len(word.strip('?!,.')) for word in text.split()])
word_count = sum(counts.values())
print "总共的单词数量: %s" % word_count

wordcount={}
for word in text.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print "单个单词出现的次数:"
print (word,wordcount)