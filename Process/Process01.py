# 进程创建
"""
多任务的实现有3种方式：
1.多进程模式
2.多线程模式
3.多进程+多线程模式

线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。

Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

进程之间是相互独立的
"""
# multiprocessing模块是跨平台版本的多进程模块，它提供了一个Process类来代表一个进程对象
from multiprocessing import Process
import os, sys
from time import sleep

# 全局变量
m = 1


# 进程创建
def task1(b, *args, **kwargs):
    global m
    try:
        n = 0
        while n < 15:
            sleep(b)
            # 调用全局变量
            m += 1
            print('任务1......', '获取当前进程ID', os.getpid(), '获取父进程ID', os.getppid(), '打印全局变量M的值', m)
            n = n + 1
        else:
            sys.exit()
    except BaseException as e:
        if isinstance(e, KeyboardInterrupt):
            pass


def task2(s, *args, **kwargs):
    global m
    try:
        n = 0
        while n < 15:
            sleep(s)
            m += 1
            print('任务2......', '获取当前进程ID', os.getpid(), '获取父进程ID', os.getppid(), '打印全局变量M的值', m)
            n = n + 1
        else:
            sys.exit()
    except BaseException as k:
        if isinstance(k, KeyboardInterrupt):
            pass


if __name__ == '__main__':
    # 获取当前进程的PID
    print(os.getpid())
    # python解释器运行就会启动进程，进程再启动p1和p2两个子进程
    # target表示所指的对象,name表示子进程的名称,args(可迭代)可变参数,传递给target指向的函数参数(*args可以接收所有类型)
    # kwargs关键字参数,封装在字典中，传递给target指向的函数kwargs = {'name': 'cc', 'age': 18}(**kwargs只能接收字典)
    p1 = Process(target=task1, name='开始运行任务一', args=(1,))
    # 启动进程，并调用该子进程中的p.run()
    p1.start()
    # 调用进程的名称
    print(p1.name)
    # 进程的PID
    print(p1.pid)
    # 终止进程
    # p1.terminate()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    # p1.join()
    # 子进程
    p2 = Process(target=task2, name='开始运行任务二', args=(1,))
    p2.start()
    print(p2.name)
    print(p2.pid)
    # p2.terminate()
    # p2.join()

"""
帮助文档：
    https://www.cnblogs.com/ywk-1994/p/9447292.html
    https://blog.csdn.net/weixin_49111957/article/details/108130260
"""


#
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     # 启动子进程
#     p.start()
#     # join方法等待子进程结束后再继续往下运行，通常用于进程间的同步
#     p.join()
#     print('Child process end.')
#
# print('-----------------------------------')
#
# import threading
#
# # 创建全局ThreadLocal对象：
# local_school = threading.local()
#
#
# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
#
# def process_thread(name):
#     # 绑定ThreadLocal的student
#     local_school.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()