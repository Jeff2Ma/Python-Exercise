
> 题目:第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如下所示：

	<?xml version="1.0" encoding="UTF-8"?>
	<root>
	<students>
	<!-- 
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
	-->
	{
   	 	"1" : ["张三", 150, 120, 100],
   	 	"2" : ["李四", 90, 99, 95],
    	"3" : ["王五", 60, 66, 68]
	}
	</students>
	</root>

## 要点记录

### dist 与 json 的格式转换

JSON到字典转化：

	ret_dict = simplejson.loads(json_str)

字典到JSON转化：

	json_str = simplejson.dumps(dict)

## dist 中文编码的问题

在python 下面一个包含中文字符串的列表（list）或字典，可以采用如下方式：

	json.dumps(dict, encoding="UTF-8", ensure_ascii=False)

## 说明

本题目做出的效果略有瑕疵，在于中文编码上的异常坑爹处理（dist 中文编码），遍寻无果，只好这样了（见生成的xml文件）

## 参考

http://blog.csdn.net/kiki113/article/details/4083756