import re
'''
写一个函数，它使用正则表达式， 确保传入的口令字符串是强口令。 强口令的
定义是： 长度不少于 8 个字符， 同时包含大写和小写字符， 至少有一位数字。你可
能需要用多个正则表达式来测试该字符串， 以保证它的强度
'''
password = input('please input a strong password:')
def checkpwd(pwd):
    strlen = len(pwd)
    checkcuppercase = re.compile(r'.*[A-Z]+.*')
    checkresult1 = checkcuppercase.search(pwd)
    checklowercase = re.compile(r'.*[a-z]+.*')
    checkresult2 = checklowercase.search(pwd)
    checknumber = re.compile(r'.*\d{1}.*')
    checkresult3 = checknumber.search(pwd)
    if((strlen) >= 8 and (checkresult1 != None) and (checkresult2 != None) and (checkresult3 != None)):
        print('input password is strong')
    else :
        print('input password is not strong')

checkpwd(password)
'''
写一个函数，它接受一个字符串， 做的事情和 strip()字符串方法一样。如果只
传入了要去除的字符串， 没有其他参数， 那么就从该字符串首尾去除空白字符。否
则， 函数第二个参数指定的字符将从该字符串中去除
'''
str1 = input('input the original string:')
str2 = input('inout the removed string:')
def removestring(str1,str2=''):
    a = '^\s*'
    b = '\s*$'
    if(str2 == ''):
        newstr = re.sub(r'%s|%s'%(a,b),'',str1)
        print('you do not input a string , remove the space auto')
    else:
        newstr = re.sub(str2,'',str1)
        print('string'+str1+'is removed from'+str2)
    return newstr
if(str2 in str1):
    strresult = removestring(str1,str2)
    print(strresult)
else:
    print('the remove string you input is not in the original string or is not a continuous')
