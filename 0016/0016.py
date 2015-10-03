#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""

第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中

"""
import xlwt

content = open('numbers.txt').read()

# 关键点
content =list(eval(content))

print content,len(content)
print content[0],len(content[0])
print content[0][0]

file = xlwt.Workbook()

table = file.add_sheet('new-sheet',cell_overwrite_ok=True)

for id in range(len(content)):
    # table.write(行,列,value)
    table.write(id,0,id+1)
    for val in range(len(content[id])):
        table.write(id,val,content[id][val])
        val = val + 1
    id = id + 1

file.save('numbers.xls')
