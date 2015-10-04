#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
    "1" : ["张三", 150, 120, 100],
    "2" : ["李四", 90, 99, 95],
    "3" : ["王五", 60, 66, 68]
}
</students>
</root>
"""

import xlrd,simplejson,sys,codecs
from xml.dom import minidom

reload(sys)
sys.setdefaultencoding('utf-8')

data = xlrd.open_workbook('../0014/student.xls', encoding_override="utf-8")

table = data.sheets()[0]    #通过索引顺序获取

nrows = table.nrows
ncols = table.ncols

print nrows, ncols

list1 = []
list2 = []

# 构造list1
for i in range(nrows):
    i = i + 1
    list1.append(str(i))

# 构造list2
for j in range(nrows):
    value = table.row_values(j)
    j = j + 1
    #print i
    print value
    list2.append(value)

print list1,list2

# 合成为 dict
d = dict(zip(list1,list2))
dd = simplejson.dumps(d, encoding="utf-8", ensure_ascii=False)
print d,dd

# 创建文件
doc = minidom.Document()

# 加入注释
xml_comment = '\n学生信息表\n"id" : [名字, 数学, 语文, 英文]\n'
doc.appendChild(doc.createComment(xml_comment))

# 创建属性
book = doc.createElement('root')
doc.appendChild(book)

# 创建嵌套属性并填入值
cotent = doc.createElement('student')
cotent.appendChild(doc.createTextNode(str(d)))
book.appendChild(cotent)

# toxml()输出紧凑格式的XML文本，toprettyxml()输出美化后的XML文本
print doc.toprettyxml()

# 生成xml 文件
file_handle = codecs.open('student.xml', 'w', 'utf-8');
doc.writexml(file_handle,indent='  ',addindent = '  ',newl='\n', encoding='utf-8')
file_handle.close()