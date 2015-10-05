#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)

参考代码

"""

import urllib,re

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print "%.2f%%"% percent


def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def get_img(html):
    reg = r'src="(.*?\.jpg)" bdwater='
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    i = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg'%i,callbackfunc)
        i+=1
html = get_html('http://tieba.baidu.com/p/2166231880')
print get_img(html)