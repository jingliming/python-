'''
python 使用正则表达式进行匹配步骤
1、导入正则表达式模块
2、创建匹配
3、调用查找方法，返回查找结果
4、查找结果使用group方法获取
'''
import re
numbercatch = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
result = numbercatch.search('this is a number as 1234-567-890')
print(result.group())