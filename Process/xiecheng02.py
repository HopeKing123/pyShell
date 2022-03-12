# -- coding: utf-8 --
# 协程greenlet和gevent 猴子补丁
"""
安装：
    pip install greenlet
    pip install gevent
"""

# 模拟协程二
# 使用greenlet模拟协程(人工通过循环切换协程)


import time

import gevent
from greenlet import greenlet
from gevent import monkey

# # 任务A
# def a():
#     for i in range(5):
#         print('A' + str(i))
#         # 休眠前切换到b
#         gb.switch()
#         time.sleep(0.1)
#
#
# # 任务B
# def b():
#     for i in range(5):
#         print('B' + str(i))
#         # 休眠前切换到c
#         gc.switch()
#         time.sleep(0.1)
#
#
# # 任务C
# def c():
#     for i in range(5):
#         print('C' + str(i))
#         # 休眠前切换到C
#         ga.switch()
#         time.sleep(0.1)


# if __name__ == '__main__':
#     # 传入目标函数
#     ga = greenlet(a)
#     gb = greenlet(b)
#     gc = greenlet(c)
#
#     # 调用
#     ga.switch()


# 模拟协程三
# 使用gevent模拟协程(自动切换协程)，及猴子补丁

# 猴子打补丁
monkey.patch_all()

"""
猴子补丁主要有以下几个用处：
在运行时替换方法、属性等
在不修改第三方代码的情况下增加原来不支持的功能
在运行时为内存中的对象增加patch而不是在磁盘的源代码中增加
"""


# 任务A
def a():
    for i in range(5):
        print('A' + str(i))
        time.sleep(0.1)


# 任务B
def b():
    for i in range(5):
        print('B' + str(i))
        time.sleep(0.1)


# 任务C
def c():
    for i in range(5):
        print('C' + str(i))
        time.sleep(0.1)


if __name__ == '__main__':
    # 创建一个greenlet对象传入相应参数，并允许。
    # spawn参数(function, *args, **kwargs)
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)

    # 子进程运行结束后主进程再运行
    g1.join()
    g2.join()
    g3.join()

    print('END')


"""
帮助文档：
https://www.jianshu.com/p/f1060b22aab8
"""
