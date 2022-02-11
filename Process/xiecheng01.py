# -- coding: utf-8 --
# 协程: 微线程
"""
进程 > 线程 > 协程
耗时操作会用到协程。
"""
import time


# 模拟协程一
def task1():
    for i in range(3):
        print('A' + str(i))
        yield
        time.sleep(2)


def task2():
    for i in range(3):
        print('B' + str(i))
        yield
        time.sleep(2)


if __name__ == '__main__':
    g1 = task1()
    g2 = task2()

    while True:
        try:
            # 输出迭代器对象，循环执行输出迭代器下一个元素
            next(g1)
            next(g2)
        except:
            break

"""
帮助文档：
https://www.runoob.com/python3/python3-iterator-generator.html
"""
