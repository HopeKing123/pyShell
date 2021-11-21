# 读文件
"""
    文件上传
    保存log

系统函数：
    open(file, mode='r', buffering=None, encoding=None)
mode模式：
    'r'       打开读取(默认)
    'w'       打开文件， 首先截断文件
    'x'       创建一个新文件并打开它进行写入
    'a'       打开以进行写入，如果存在则附加到文件末尾
    'b'       二进制模式
    't'       文本模式（默认）
    '+'       打开磁盘文件进行更新（读写）

注意：读取图片将会输出二进制，mode = 'rb'
"""
# 打开读取a.txt文件,open打开文件会返回流所以需要接收一下
stream = open(r'I:\p1\a.txt', 'r')

# container = stream.read()
# print(container)

# readable: 判断文件是否可以读取
# result = stream.readable()
# print(result)

# readline: 若已经读过一次文件，则使用readline将无法在读取出文件，因为指针光标在最后位了，
# 所以若要读行则放置在最前面
# result = stream.readline()
# print(result)

# readlines: 内容保存在列表中
lines = stream.readlines()
print(lines)

