import os
import re

def FileStringReplace(_file_string_):
    fstrlist = _file_string_.split(' ')
    print(fstrlist)
    replist = re.findall(r'[A-Z]{2,}\.?',_file_string_)
    print(replist)
    for rep in replist:
        restring = input('Enter %s:'%rep)
        fstrlist.insert(fstrlist.index(rep),restring)
        fstrlist.remove(rep)
    _result_string_ = ' '.join(fstrlist)
    filewrite = open('result.txt', 'w+')
    filewrite.write(_result_string_)
    filewrite.close()
    #return _result_string_

path = 'E:/python project/python3/python-/test.txt'
if(os.path.isfile(path)):
    fileread = open(path)
    _file_string_ = fileread.read()
    fileread.close()
    FileStringReplace(_file_string_)

    fileread = open('result.txt','r')
    _result_string_ = fileread.read()
    print(_result_string_)
