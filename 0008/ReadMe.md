# 要点记录

## 题目


## html2text模块

查到了互联网之子写的 [html2text](https://github.com/aaronsw/html2text) 模块，但这个虽然在Github 上写着"html2text is a Python script that converts a page of HTML into clean, easy-to-read plain ASCII text. "，但转出来的却是Markdown 格式的，不符合我们要求纯文本的要求啊。也有人开了个[issues](https://github.com/aaronsw/html2text/issues/71) 探讨这个问题，可惜Aaron Swartz 早已看不到了。

## 遇到UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 0: ordinal not in range(128) 的问题

解析时候编码问题,加上`.decode('utf-8')`即可

## Beautiful Soup 模块

见参考处的文档说明，本题最后是用这个的。

## 参考

http://beautifulsoup.readthedocs.org/zh_CN/latest/