import re
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
