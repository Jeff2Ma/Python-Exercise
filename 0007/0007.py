#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

import re, os, fnmatch

def Count_line(file_name):
    count = 0 # 总的行数
    empty_line = 0 #空行行数
    single_comment_line = 0 # 单行注释行数
    skip = False
    count_mini = 0
    for file_line in open(file_name).xreadlines():
        if file_line == '' or file_line == '\n': #空行检测
            empty_line += 1
        # 匹配单行注释的情况
        elif re.match('#', file_line) != None:
            single_comment_line += 1
        count += 1

        #以下统计没有注释的情况
        file_line = file_line.strip()
        if file_line:
            if file_line.startswith('#'):
                continue
            if file_line.startswith('"""'):
                skip = not skip
                continue
            if not skip:
                count_mini += 1
    comment_line =  count - count_mini
    print "文件%s 的代码总行数:%s,空行行数:%s,注释行数:%s" % (file_name, count, empty_line, comment_line)

# 遍历目标目录下的相关文件
def Find_file(root='.', recurse=True, pattern='*'):
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path, name)
        if not recurse:
            break

if __name__ == '__main__':
    recurse = True
    for files in Find_file("..", recurse, '*.py'):
        Count_line(files)
