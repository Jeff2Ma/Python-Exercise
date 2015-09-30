#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""
题目:敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""

filtered_file = open("filtered_words.txt")
filtered_word = filtered_file.read().split()
inputed_words = raw_input(u"请输入相关内容,按回车键结束:".encode("utf-8"))
for word in filtered_word:
    if inputed_words.find(word) == 0:
        print inputed_words.replace(word,'**')
        quit()

print inputed_words
