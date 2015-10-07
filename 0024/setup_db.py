#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""
安装相关数据库的数据
"""
import sqlite3
con = sqlite3.connect('./db/todo.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
con.execute("INSERT INTO todo (task,status) VALUES ('看python 的一节书',0)")
con.execute("INSERT INTO todo (task,status) VALUES ('看电影《康囧》',1)")
con.execute("INSERT INTO todo (task,status) VALUES ('读书《从1到11》',1)")
con.execute("INSERT INTO todo (task,status) VALUES ('学习课程《单身狗的修养》',0)")
con.commit()