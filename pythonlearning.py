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

#正则表达式总结
#?匹配零次或一次前面的分组。
#*匹配零次或多次前面的分组。
#+匹配一次或多次前面的分组。
#{n}匹配 n 次前面的分组。
#{n,}匹配 n 次或更多前面的分组。
#{,m}匹配零次到 m 次前面的分组。
#{n,m}匹配至少 n 次、至多 m 次前面的分组。
#{n,m}?或*?或+?对前面的分组进行非贪心匹配。
#^spam 意味着字符串必须以 spam 开始。
#spam$意味着字符串必须以 spam 结束。
#.匹配所有字符，换行符除外。
#\d、 \w 和\s 分别匹配数字、单词和空格。
#\D、 \W 和\S 分别匹配除数字、单词和空格外的所有字符。
#[abc]匹配方括号内的任意字符（诸如 a、 b 或 c）。
#[^abc]匹配不在方括号内的任意字符

#使用sub进行内容替换
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

#通配符.  .*可以匹配所有字符

#re.VERBOSE 来编写注释
#re.IGNORECASE 来忽略大小写
#re.DOTALL来匹配包换换行符在内的所有字符