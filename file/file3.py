# 文件复制
"""
源文件：I:\p1\a.txt
目标文件：I:\p2\a.txt

with 结合open使用，可以帮助我们自动释放资源

绝对路径：路径是必须全部输出的
相对路径：可省略部分路径
开发中用相对路径较多
"""
# write()方法可将任何字符串写入一个打开的文件。自动关闭连接回收内存
# stream = open(r'I:\p1\a.txt', 'rb')
# 如果指定的文件不存在则自动创建
with open(r'I:\p1\a.txt', 'rb') as stream:
    container = stream.read()  # 读取文件内容

    with open(r'I:\p2\a.txt', 'wb') as wstream:
        wstream.write(container)

print("文件复制完成")

# 批量复制文件,目录操作类库shutil
import shutil
# 复制文件
shutil.copyfile('I:\p1\\a.txt', 'I:\p2\\a.txt')
# 复制目录
shutil.copytree('I:\p1','I:\p2')