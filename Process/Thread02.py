# -- coding: utf-8 --
# 线程锁
"""
进程和线程
进程：计算密集型
线程：耗时操作(爬虫，IO)

进程：
进程是由若干线程组成的，一个进程至少有一个线程。
多任务可以由多进程完成，也可以由一个进程内的多线程完成。
由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，需要使用threading这个高级模块。

线程：(python的线程式"伪线程")
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多进程中，所有变量都由线程共享，所以，任何一个变量都可以被任何一个线程修改，因此线程之间共享数据最大的危险在于多个线程同时改变一个变量，会把内容给该乱了。
线程状态：
    新建 就绪 运行 阻塞 结束

锁(GIL)：全局解释器锁
    python解释器在执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
    这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

好处：确保了某段关键代码只能由一个线程从头到尾完整地执行，
坏处：阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率大大地下降了。
    其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
"""

import threading
import time

# 线程锁一


# 全局变量
n = 0

# 创建锁
look1 = threading.Lock()


def task1():
    global n
    look1.acquire()
    try:
        for i in range(1000000):
            # 先要获取锁(当多个线程同时执行lock.acquire()时，只有一个线程能成功的获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止)
            n += 1
        print('task1中n的值是: ', n)
    finally:
        look1.release()


def task2():
    global n
    look1.acquire()
    try:
        for i in range(1000000):
            # 先要获取锁(当多个线程同时执行lock.acquire()时，只有一个线程能成功的获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止)
            n += 1

        print('task2中n的值是: ', n)
    finally:
        look1.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

print('最后打印的n: ', n)

print('-------------------------------------------')


# 线程锁二（模拟银行存取钱）

# 多个线程同时操作一个全局共享变量
# 存款余额
balance = 0
# 创建一个锁
look = threading.Lock()


# 计算公式函数
def change_it(n):
    # 先存后取，结果应该为0：
    global balance
    # 如下计算语句在CPU执行时会分为若干条语句(1.计算balance + n，存入临时变量中；2.将临时变量的值赋给balance)
    balance = balance + n
    # print(balance)
    balance = balance - n
    # print(balance)


# 定义运行线程函数
def run_thread(n):
    # 共循环200万次，每循环一次调用一次change_it计算公式函数进行计算.
    for i in range(2000000):
        # 先要获取锁(当多个线程同时执行lock.acquire()时，只有一个线程能成功的获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止)
        look.acquire()
        # 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
        try:
            # 接收函数参数，传递给change_it计算公式函数
            change_it(n)
        finally:
            # 释放锁
            look.release()


# 创建线程，定义args=可变变量参数，传入目标函数run_thread函数参数.
t11 = threading.Thread(target=run_thread, args=(5,))
t22 = threading.Thread(target=run_thread, args=(8,))
# 启动
t11.start()
t22.start()
# 等待子线程执行完成后再执行主进程.
t11.join()
t22.join()
# 理论上打印的结果应该为0，但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
print(balance)
"""
出现不符合预期条件的结果原因在于，执行修改balance需要多条语句的执行，而在执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。
两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成了负数，所以，我们必须确保一个线程在修改balance的时候，别的线程一定不能改。
如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。
由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：
"""

"""
学习文档：
https://www.liaoxuefeng.com/wiki/1016959663602400/1017629247922688
"""
