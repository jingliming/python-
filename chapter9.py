import shutil,os
import zipfile

'''
shutil.copy(src,dst) 复制文件夹
shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,ignore_dangling_symlinks=False) 复制整个文件夹
shutil.move(src, dst, copy_function=copy2) 文件和文件夹的移动
shutil.rmtree(path, ignore_errors=False, onerror=None) 删除整个文件夹和文件
os.unlink(path) 删除一个文件
os.rmdir(path) 删除一个空文件夹
os.walk(top, topdown=True, onerror=None, followlinks=False) 遍历文件夹
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
fileinfo = zipfile.ZipFile(filepath) 打开一个zip文件
fileinfo.namelist()  获取zip文件列表
subfileinfo = fileinfo.getinfo(filepath) 获取压缩文件信息
subfileinfo.file_size
subfileinfo.compress_size
fileinfo.extractall()将压缩文件全部解压缩
fileinfo.extract()将指定文件解压缩
fileinfo.close()
fileinfo = zipfile.ZipFile(filepath,'w') 打开一个zip文件
fileinfo.write()写文件
'''