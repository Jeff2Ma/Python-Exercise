## 要点记录

> 题目:敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。


## python字符串查找(find)

看下文档解释：

string.find(s, sub[, start[, end]])
Return the lowest index in s where the substring sub is found such that sub is wholly contained in s[start:end]. Return -1 on failure. Defaults for start and end and interpretation of negative values is the same as for slices

后面的[]是表示可选项，start,end表示查找字符串的开始位置和结束位置。

比如下面的例子：

	info = 'abca'
	print info.find('a')

返回的结果是：0

	info = 'abca'
	print info.find('a',1)

返回的结果是：3

	info = 'abca'
	print info.find('333')
	
返回的结果是：-1

## 字符串替换函数 replac()

比较简单不多解释