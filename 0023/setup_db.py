#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""
安装相关数据库的数据
"""

import sqlite3
con = sqlite3.connect('./db/comment.db')

con.execute("CREATE TABLE comments (id INTEGER PRIMARY KEY, name char(40) NOT NULL, comment char(200) NOT NULL, date_time date DEFAULT (datetime('now','localtime')) NOT NULL)")
con.execute("INSERT INTO comments (name,comment) VALUES ('张三','不错不错不错，很好很好')")
con.execute("INSERT INTO comments (name,comment,date_time) VALUES ('李四','欢迎加入xxx，我们即将大范德萨','2015-10-03')")
con.execute("INSERT INTO comments (name,comment,date_time) VALUES ('wangwu','阿斯顿发阿凡阿斯顿发阿凡达的东东阿斯顿发阿凡达的东东达的东东','2015-10-05')")
con.execute("INSERT INTO comments (name,comment,date_time) VALUES ('阿姆罗','weclome to chinesdrs, i will go.','2015-10-07')")
con.commit()

"""
测试
"""
c = con.cursor()
c.execute("SELECT name,comment,date_time FROM comments ORDER BY id")
result = c.fetchall()
c.close()
print result