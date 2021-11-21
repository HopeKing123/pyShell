# os.path中函数
import os

# 	判断是否为绝对路径
# r = os.path.isabs('I:\p1\\a,txt')
# print(r)  # true

# 通过相对路径获取绝对路径
# path = os.path.abspath('a.txt')
# print(path)

# 获取当前文件的绝对路径
# path = os.path.abspath(__file__)
# print(path)

# 获取当前文件的目录
# path = os.getcwd()
# print(path)

# split把路径分割成 dirname 和 basename，返回一个元组
path = r'F:\pyShell\os\os2.py'
result = os.path.split(path)
print(result)
print(result[1])

# splitext分割路径，返回路径名和文件扩展名的元组
result = os.path.splitext(path)
print(result)

# getsize 返回文件的大小,单位是字节
size = os.path.getsize(path)
print(size)

# exists 如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。
a = os.path.exists('I:\p1')
print(a)

# isdir 判断路径是否为目录
c = os.path.isdir(r'I:\p1')
print(c)

# 其他os.path功能见官网

