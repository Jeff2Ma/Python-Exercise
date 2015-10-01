# 要点记录

> 题目：纯文本文件 student.txt 为学生信息, 里面的内容（包括花括号）如下所示：

	{
    	"1":["张三",150,120,100],
    	"2":["李四",90,99,95],
    	"3":["王五",60,66,68]
	}
> 请将上述内容写到 student.xls 文件中

## Python 中Json 的解析

题目中的txt 文档就是Json 数据，解析的话可以借助simplejson 模块。看了下语法还算是简单的。

为了避免在txt 中插入Json 数据导致出现标点符号会改变的问题，就原题的txt 格式之间改为了json 文件格式。

## 涉及到的知识点

相关模块的运用

数据类型转换（本题用到了数值转化为字符串）

## 参考

http://blog.csdn.net/gexiaobaohelloworld/article/details/7948474

http://liluo.org/blog/2011/01/python-using-xlrd-xlwt-operate-excel/