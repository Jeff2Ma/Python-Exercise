#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""
第 0024 题： 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。

"""

import sqlite3, sys, sae
from bottle import route, run, debug, template, request, static_file, error, redirect

app = Bottle()

# 强制编码
reload(sys)
sys.setdefaultencoding('utf8')

# 全局连接数据库
conn = sqlite3.connect('db/todo.db')

# 中文编码hack
conn.text_factory = str


# ----------------------------------------------------
# 首页
@route('/')
@route('/todo')
def todo_list():
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template("tpl/make_table", rows=result)
    return output

# ----------------------------------------------------
# 已完成页面
@route("/done")
def show_done():
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE 0")
    result = c.fetchall()
    c.close()
    output = template("tpl/show_done", rows=result)
    return output

# ----------------------------------------------------
# 新建任务
@route('/new', method='GET')
def new_item():
    if request.GET.get('save','').strip():
        new = request.GET.get('task', '').strip()
        c = conn.cursor()
        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid
        conn.commit()
        c.close()
        output = template("tpl/notice",msg = '已添加到数据库中！' , no=new_id)
        return output
    else:
        return template('tpl/new_task.tpl')

# ----------------------------------------------------
# 编辑
@route('/edit/:no', method='GET')
def edit_item(no):
    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        status = request.GET.get('status','').strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?" ,(edit, status, no))
        conn.commit()

        output = template("tpl/notice",msg = '已成功更新！' , no=no)
        return output
    else:
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?" ,[str(no)])
        cur_data = c.fetchone()

        return template('tpl/edit_task', old=cur_data, no=no)



@route('/help')
def help():
    return static_file('help.html', root='static/')

@route('/json:json#[1-9]+#')
def show_json(json):
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task':'对应的待办事项不存在'}
    else:
        return {'Task': result[0]}

@error(403)
def mistake403(code):
    return '参数格式错误！'

@error(404)
def mistake404(code):
    return '该页面不存在！'

@route('/static/:filename')
def serve_static(filename):
    return static_file(filename, root='./static/')

debug(True)
run(host='localhost', port=8800, reloader=True)

application = sae.create_wsgi_app(app)