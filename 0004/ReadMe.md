# 要点记录

> 注：此题本解答方案（代码）不知道对不对


## 一些函数

- strip()

Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。

- split()

Python split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串

## 相关库

### collections模块的Counter类

常用操作：

	sum(c.values())  # 所有计数的总数
	c.clear()  # 重置Counter对象，注意不是删除
	list(c)  # 将c中的键转为列表
	set(c)  # 将c中的键转为set
	dict(c)  # 将c中的键值对转为字典
	c.items()  # 转为(elem, cnt)格式的列表
	Counter(dict(list_of_pairs))  # 从(elem, cnt)格式的列表转换为Counter类对象
	c.most_common()[:-n:-1]  # 取出计数最少的n个元素
	c += Counter()  # 移除0和负值


## 参考

http://stackoverflow.com/questions/4895157/counting-the-word-length-in-a-file

http://www.pythoner.com/205.html

http://stackoverflow.com/questions/21107505/python-word-count-from-a-txt-file-program?newreg=b491dbc6d7854eda90e20c8eb305a71d
