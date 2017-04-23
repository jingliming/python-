import os


'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
路径操作

os.getcwd() 获取当前工作目录
os.chdir()  更改当前工作目录
os.mkdir()  创建文件夹
绝对路径和相对路径
单个点指的是当前文件夹，两个点指的是父文件夹
os.path.abspath(path) 获取直到当前路径的绝对路径
os.path.isabs(path)  判断传入的路径信息是否是绝对路径
os.path.relpath(path,start) 获取指定的start开始到pathd的相对路径
os.path.dirname(path) 获取最后一个斜杠前面的目录字符串
os.path.basename(path) 获取最后一个斜杠后面的文件名称字符串
os.path.split(path) 将目录最后一个斜杠之前的目录和后面的文件名分开并放在一个元组中
如果需要将目录中的所有文件夹都进行分割，需要
filedir = 'E:\python project\python3\python-'
print(filedir.split(os.path.sep))
最后结果为
['E:', 'python project', 'python3', 'python-']
os.path.getsize(path)  获取目录对应文件的大小
print(os.listdir('E:')) 获取目录中的所有文件列表
os.path.exists(path)  判断提供的目录是否存在
os.path.isdir(path)  判断目录所对应的是否是一个文件夹
os.path.isfile(path) 判断目录所对应的是否是一个文件

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
文件读写

filedir = 'E:\python project\python3\python-\README.md'
filename = open(filedir,encoding='utf-8')
filestr = filename.read()
print(filestr)
写文件可以使用write，可以在第二个参数使用‘w’或者‘a’追加写
关闭文件使用close
主意：write函数不会默认添加换行，需要自己手动添加'\n'
'''