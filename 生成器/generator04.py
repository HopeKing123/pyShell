"""
生成器：generator  取代了列表推导式，节省空间。在使用的情况下生成结果。不适用则不生成
定义生成器的方式：
    1.通过列表推导式的方式定义生成器
    2.在函数中包含关键字yield那么这个函数就不在是普通的函数而是生成器函数
产生元素：
    1. next(generator)  每次调用都会产生一个新的元素，弱国元素产生完毕，再次调用的话就会产生异常
    2.生成器自己的方法：__next() sed(value)

普通函数和generator函数的区别：
1.普通函数调用直接返回结果
r = abs(6)
r
2.generator函数的调用实际返回一个generator对象
g = fib(6)
g
<generator object fib at 0x1022ef948>
"""


# 进程-》线程-》协程

# 生成器的协程应用
def task1(n):
    for i in range(n):
        print("正在搬第{}块砖".format(i))
        yield None          # 生成器


def task2(n):
    for i in range(n):
        print("正在听第{}几首歌".format(i))
        yield None          # 生成器


g1 = task1(5)
g2 = task2(5)

# 同时执行
while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break
