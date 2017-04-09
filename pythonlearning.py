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


#使用括号进行分组

groupmatch = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d)')
result = groupmatch.search('this is group of number 123-4567-890')
print(result.group(1))
print(result.group(2))
print(result.group(0))
print(result.group())

#利用管道匹配第一个出现的字符串

gap = re.compile(r'Bat(man|monile|women)')
result = gap.search('Batman is me')
print(result.group())
print(result.group(1))

#使用?进行选择匹配也可以叫做零次或者一次匹配
rexsearch = re.compile(r'(\d\d\d-)?\d\d\d\d-\d\d\d')
result = rexsearch.search('this is 123-4567-890')
print(result.group())
result = rexsearch.search('this is 4567-890')
print(result.group())


#使用*进行选择匹配也可以叫做零次或者多次匹配
rexsearch = re.compile(r'\d\d\d-(\d\d\d\d-)*\d\d\d')
result = rexsearch.search('this is 123-4567-890')
print(result.group())
result = rexsearch.search('this is 123-890')
print(result.group())
result = rexsearch.search('this is 123-4567-4567-890')
print(result.group())


#使用+进行选择匹配也可以叫做一次或者多次匹配
rexsearch = re.compile(r'\d\d\d-(\d\d\d\d-)+\d\d\d')
result = rexsearch.search('this is 123-4567-890')
print(result.group())

#使用{}进行指定次数的匹配
rexsearch = re.compile(r'\d\d\d-(\d\d\d\d-){3}\d\d\d')
result = rexsearch.search('this is 123-4567-4567-4567-890')
print(result.group())
rexsearch = re.compile(r'\d\d\d-(\d\d\d\d-){3,5}\d\d\d')
result = rexsearch.search('this is 123-4567-4567-4567-4567-890')
print(result.group())
rexsearch = re.compile(r'\d\d\d-(\d\d\d\d-){,5}\d\d\d')
result = rexsearch.search('this is 123-4567-890')
print(result.group())

#贪心匹配
#python默认匹配满足条件的最长匹配原则，也就是“贪心”的
#非贪心匹配
#在{}?为非贪心匹配，会匹配满足条件最短的结果

#findall实现全部匹配而不是第一次匹配
groupmatch = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d)')
result = groupmatch.findall('this is group of number 123-4567-890 and 333-4444-555')
print(result)