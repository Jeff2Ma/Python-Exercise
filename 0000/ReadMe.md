## 题目要点记录

> 题目：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

![头像](http://i.imgur.com/sg2dkuY.png?1)

本题目一开始使用Mac 环境做题，但发现挖坑无数，后转到Windows 平台。

### 【Mac】安装PIL报错

	pip install PIL --allow-external PIL --allow-unverified PIL

### 【Mac】报错：IOError: decoder jpeg not available 的解决方法

无解，后面已经转到Win 平台

### 【Windows】下im.show() 后显示“正在加载...”的解决方法

打开安装路径相关文件，如D:\Python27\Lib\site-packages\PIL\ImageShow.py

约99 行改为如下：

	def get_command(self, file, **options):
            #return "start /wait %s && del /f %s" % (file, file)
            return "start /wait %s && PING 127.0.0.1 -n 5 > NUL && del /f %s" % (file, file)


### 【Windows】报错“ImportError: The _imagingft C module is not installed

官网下载的PIL 安装包有问题，先在机子上卸载后重新安装附带的exe文件

### 参考文章

http://stackoverflow.com/questions/16373425/add-text-on-image-using-pil

http://yongyuan.name/pcvwithpython/chapter1.html