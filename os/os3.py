# os模块中功能
import os

# 获取当前文件的目录
# path = os.getcwd()
# print(path)

# listdir返回path指定的文件夹包含的文件或文件夹的名字的列表。
# all = os.listdir(r'I:\p1')
# print(all)

# mkdir创建文件夹
# os.mkdir(r'I:\p2')

# 判断文件夹是否存在，不存在则创建
# if not os.path.exists(r'I:\p2'):
#     f = os.mkdir(r'I:\p2')
#     print(f)

# rmdir删除文件夹,只能移 除空文件夹,有文件则报错
# os.rmdir(r'I:\p2')

# removedirs递归删除目录，只能一层一层删除目录，否则报错
# os.removedirs(r'I:\p2\awdaw')

# remove删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
# os.remove(r'I:\p2\aw.txt')

# 删除层级文件夹p3,
# path = r'I:\p2\p3'
#
# filelist = os.listdir(path)  # ['1.txt','2.txt','3.txt',]
#
# for file in filelist:
#     path1 = os.path.join(path, file)
#     os.remove(path1)
# else:
#     os.rmdir(path)
# print('删除成功')

# chdir 切换目录
# os.chdir(r'c:\p1')

# system() 与操作系统进行交互的功能
# os.system(dir -l)
