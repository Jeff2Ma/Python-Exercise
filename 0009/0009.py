#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""
第 0008 题：一个HTML文件，找出里面的链接。
"""

import urllib2
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
content = urllib2.urlopen('http://devework.com/').read().decode('utf-8')
#目标区域
only_body = SoupStrainer("body")
soup = BeautifulSoup(content, "html.parser", parse_only=only_body)
for link in soup.find_all('a'):
    print(link.get('href'))

