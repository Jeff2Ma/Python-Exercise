#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""
纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中

"""
import simplejson as json
import xlwt

content = open('student.json').read()

ddata = json.loads(content)

file = xlwt.Workbook(encoding = 'utf-8')

"""
如果对一个单元格重复操作，会引发
returns error:
Exception: Attempt to overwrite cell:
sheetname=u'sheet 1' rowx=0 colx=0
所以在打开时加cell_overwrite_ok=True解决
"""
table = file.add_sheet('new-sheet',cell_overwrite_ok=True)

for id in range(len(ddata)):
    # table.write(行,列,value)

    table.write(id,0,id+1)
    for val in range(len(ddata[str(id+1)])):
        table.write(id,val,ddata[str(id+1)][val])
        val = val + 1
    id = id + 1

file.save('student.xls')