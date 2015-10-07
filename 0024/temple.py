#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""
 bottle 的基本用法
"""

from bottle import route, error, post, get, run, static_file, abort, redirect, response, request, template

@route('/')
@route('/index.html')
def index():
    return '<a href="/hello">/hello</a><br><a href="/hello-again">/hello-again</a>'

@route('/hello')
def hello():
    return '<h1>HELLO WOLRD</h1>'

@route('/hello-again')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"

@route('/hello/:name')
def hello_name(name):
    page = request.GET.get('page', '1')
    return '<h1>HELLO %s <br/>(%s)</h1>' % (name, page)

@route('/static/:filename')
def serve_static(filename):
    return static_file(filename, root='./static/')

@route('/raise_error')
def raise_error():
    abort(404, "error...")

@route('/redirect')
def redirect_to_hello():
    redirect('/hello')

@route('/ajax')
def ajax_resonse():
    return {'dictionary': 'you will see ajax response right? Content-Type will be "application/json"'}

@error(404)
def error404(error):
    return '404 error !!!!!'

@get('/upload')
def upload_view():
    return """
        <form action="/upload" method="post" enctype="multipart/form-data">
          <input type="text" name="name" />
          <input type="file" name="data" />
          <input type="submit" name="submit" value="upload now" />
        </form>
        """

@post('/upload')
def do_upload():
    name = request.forms.get('name')
    data = request.files.get('data')
    if name is not None and data is not None:
        raw = data.file.read() # small files =.=
        filename = data.filename
        return "Hello %s! You uploaded %s (%d bytes)." % (name, filename, len(raw))
    return "You missed a field."

@route('/tpl')
def tpl():
    return template('test')

@route('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return "<p>Aready done.</p>"

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='/path/to/static/files', download=filename)

run(host='localhost', port=8800, reloader=True)