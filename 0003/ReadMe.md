# 要点记录

> 题目:第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

本题目在于redis 与Python 的结合使用

## 在Mac 上安装、使用redis

直接用brew 快捷方便：

	brew install redis

安装成功后启动redis：

	redis-server /usr/local/etc/redis.conf

额外开个iterm 当做客户端：

	redis-cli


## 在MAC 上的Python 环境安装pyredis

	sudo pip install redis


## 代码

知道用法后就很简单，直接用for 循环保存即可。

## 参考

http://debugo.com/python-redis/