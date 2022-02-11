# -- coding: utf-8 --
# ThreadLocal：本地线程
"""
ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
"""

import threading

# 创建全局ThreadLocal(全局本地线程)对象：
local_school = threading.local()


# 定义进程学生函数
def process_student():
    # 获取当前进程关联的student(获取name)
    std = local_school.student
    # 打印 学生，以及进程名称
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


# 定义进程线程函数
def process_thread(name):
    # 绑定ThreadLocal的student等于name，局部变量
    local_school.student = name
    # 调用外部函数
    process_student()


# 创建线程(指定目标函数，args传入变量给目标函数参数进行调用，name定义线程名称)
t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')

# 启动
t1.start()
t2.start()

# 子线程执行完成后，执行主进程
t1.join()
t2.join()
