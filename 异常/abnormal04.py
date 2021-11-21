"""
情况四：（try与finally）
场景： 文件操作，数据库操作
try:
    有可能出现多种异常
except 类型1:
    如果有异常执行的代码
finally：
    无论有没有异常都会运行finally代码

注意： 若try存在return，则return不会立即执行，而是将finally执行完成后再return，
若finally也存在return则将覆盖try的return，否则传回原有值。
"""


# 示例 情况四：open读文件无论有没有异常都在finally中关闭stream流
def func():
    stream = None
    try:
        stream = open(r'I:\p1\a.txt')
        containor = stream.read()
        print(containor)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('------finally------')
        if stream:
            stream.close()
        return 3


# 调用代码
x = func()
print(x)
