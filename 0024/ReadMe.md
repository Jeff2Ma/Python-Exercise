
> 题目:第 0024 题： 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。

## 成果

使用Bottle + SQLite 制作的一个简易 todolist 应用。

## 用法

安装好相应的依赖库后，

进入目录，先安装数据库文件（如果没有）：

	python setup_db.py

然后启动：
	
	python todo.py

然后登录http://localhost:8800/ 即可。

## 目录树
	.
	├── db
	│   └── todo.db （数据库文件）
	├── setup_db.py（初始安装数据库）
	├── static（静态文件目录）
	│   ├── help.html
	│   ├── primer.css
	│   └── style.css
	├── todo.py（核心文件）
	└── tpl（模板文件）
    	├── edit_task.tpl
    	├── footer.tpl
    	├── header.tpl
    	├── make_table.tpl
    	├── new_task.tpl
    	├── notice.tpl
    	└── show_done.tpl

## 问题记录

这个基本来自于Bottle 官方的教程例子。

基本上就是Bottle + SQLite 的用法，做的过程需要不断搜索相关资料才能做出来。

### 遇到 You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that 的问题

解决方法：

	connection.text_factory = str

### 


## 参考

http://stackoverflow.com/questions/228912/sqlite-parameter-substitution-problem