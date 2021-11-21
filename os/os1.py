"""
os.path.dirname(__file__)：获取当前文件所在的文件目录(绝对路径)
__file___:表示当前文件的目录在什么位置
os.path.join(path,'') 返回的是一个拼接后的新路径
"""
import os
# 将路径以字符串的形式输出
print(os.path.dirname(__file__))

# 将文件保存在当前目录下
with open(r'I:\p1\a.txt', 'rb') as stream:
    container = stream.read()   # 读取文件内容
    # 找到最后一个\从右往左找
    file = stream.name
    filename = file[file.rfind('\\')+1:]    # 截取文件名, 在不知道文件名的情况下

    path = os.path.dirname(__file__)
    result = os.path.join(path,filename)     # a1.txt为新复制的文件名   filename
    with open(result,'wb') as wstream:
        wstream.write(container)






