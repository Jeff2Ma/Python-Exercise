#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""
第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下

所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!--
    数字信息
-->

[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]

</numbers>
</root>

"""


import xlrd,simplejson,sys,codecs
from xml.dom import minidom
reload(sys)
sys.setdefaultencoding('utf-8')

data = xlrd.open_workbook('../0016/numbers.xls', encoding_override="utf-8")

table = data.sheets()[0]    #通过索引顺序获取

nrows = table.nrows
ncols = table.ncols

print nrows, ncols

list1 = []
list2 = []

# 构造list2
for j in range(nrows):
    value = table.row_values(j)
    j = j + 1
    #print i
    print value
    list2.append(value)

print list2

d = list(list2)

# 创建文件
doc = minidom.Document()

# 加入注释
xml_comment = '\n数字信息\n'
doc.appendChild(doc.createComment(xml_comment))

# 创建属性
book = doc.createElement('root')
doc.appendChild(book)

# 创建嵌套属性并填入值
cotent = doc.createElement('numbers')
cotent.appendChild(doc.createTextNode(str(d)))
book.appendChild(cotent)

# toxml()输出紧凑格式的XML文本，toprettyxml()输出美化后的XML文本
print doc.toprettyxml()

# 生成xml 文件
file_handle = codecs.open('numbers.xml', 'w', 'utf-8');
doc.writexml(file_handle,indent='  ',addindent = '  ',newl='\n', encoding='utf-8')
file_handle.close()