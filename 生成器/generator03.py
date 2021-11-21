# 定义生成器

"""
调用生成器的方法：
1.next()
2.__next__():获取下一个元素
3.send(value)：向每次生成器调用中传值，可以传入变量。注意：第一次调用必须传空值。
"""


# 生成器示例：
def gen():
    i = 0
    while i < 5:
        temp = yield i  # 类似于 return 0 + 暂停
        print('temp', temp)
        i += 1
    return '没有更多的数据'


g = gen()

print(g.send(None))  # send必须先接收空值，才能传入value
n1 = g.send('呵呵')
print('n1:', n1)
n2 = g.send('哈哈')
print('n2', n2)
