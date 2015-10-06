#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""
第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。

(本人的是移动卡情况)
"""

import xlrd,simplejson,sys,codecs

data = xlrd.open_workbook('list.xls', encoding_override="utf-8")

table = data.sheets()[0]    #通过索引顺序获取

nrows = table.nrows
ncols = table.ncols

list =[]
min_count = 0
sec_count = 0

# 构造list
for j in range(3,nrows):
    value = table.cell(j,5).value
    j = j + 1
    #print i
    print value

    # xx分xx秒的情况
    if len(value) == 6:
        min = int(value[0:2])
        sec = int(value[3:5])
        min_count += min
        sec_count += sec

    # xx秒的情况
    if len(value) == 3:
        sec = int(value[0:2])
        sec_count += sec

all_count_sec =  min_count * 60 + sec_count


total_time_min = (all_count_sec / 60)
total_time_sec = all_count_sec - (all_count_sec / 60) * 60

print "通话时长总计:%s 分%s 秒(总共%s 秒)" % (total_time_min,total_time_sec,all_count_sec)