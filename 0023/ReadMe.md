
> 题目:第 0023 题： 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。


## 成果

使用Bottle + SQLite 制作的一个及简留言板。

## 用法

安装好相应的依赖库后，

进入目录，先安装数据库文件（如果没有）：

	python setup_db.py

然后启动：
	
	python comment.py

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
    	├── footer.tpl
    	├── header.tpl
    	├── comment_list.tpl
    	├── edit.tpl

## 问题记录

相关问题见0024 题目。