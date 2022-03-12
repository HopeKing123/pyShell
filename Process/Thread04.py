# -- coding: utf-8 --
# 生产者与消费者和死锁

# 生产者与消费者
"""
Python的queue模块中提供了同步的，线程安全的队列类，包括FIFO(先入先出)队列Queue.
LIFO(后入先出)队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原语（可以理解为原子操作，要么不做，要么做完），能够在多线程中直接使用。
可以使用队列来实现线程间的同步

"""
import threading, queue, random, time


# 定义生产者
def produce(q):
    i = 0
    # 循环十次
    while i < 10:
        # randint1-100的随机数
        num = random.randint(1, 100)
        # 往队列中传入数据.
        q.put('生产者产生数据： %d' % num)
        # 打印产生的数据.
        print('生产者产生数据： %d' % num)
        # 休眠
        time.sleep(1)
        i += 1
    # 往队列中传入None
    q.put(None)
    # 告诉消费者队列处理完成
    q.task_done()


# 定义消费者
def consume(q):
    while True:
        # 从队列中获取数据
        item = q.get()
        # 判断获取的数据是否为None，是则结束循环
        if item is None:
            break
        # 打印
        print('消费者获取到： %s' % item)
        time.sleep(4)
    # 完成任务
    q.task_done()


if __name__ == '__main__':
    # 队列最多存放10个数据
    q = queue.Queue(10)
    arr = []

    # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    # 创建消费者
    tc = threading.Thread(target=consume, args=(q,))
    tc.start()

    th.join()
    tc.join()
    print('END')


# 死锁
"""
死锁：
    多个锁长时间未释放，进程或线程互相抢占等待会产生死锁
避免死锁：
    1.重构代买
    2.timeout超时

"""

# 模拟产生死锁

# from threading import Thread, Lock
# import time
#
# lockA = Lock()
# lockB = Lock()
#
#
# # 自定义线程1
# class MyThread1(Thread):
#     def run(self) -> None:
#         if lockA.acquire():  # 如果可以获取到锁则返回True
#             print(self.name + '获取了A锁')
#             time.sleep(0.1)
#             if lockB.acquire(timeout=5):  # 会出现阻塞,加参数timeout可解决阻塞
#                 print(self.name + '又获取了B锁，原来还有A锁')
#                 # 释放B锁
#                 lockB.release()
#         # 释放A锁
#         lockA.release()
#
#
# # 自定义线程2
# class MyThread2(Thread):
#     def run(self) -> None:
#         if lockB.acquire():  # 如果可以获取到锁则返回True
#             print(self.name + '获取了B锁')
#             time.sleep(0.1)
#             if lockA.acquire(timeout=5):  # 会出现阻塞,加参数timeout可解决阻塞
#                 print(self.name + '又获取了A锁，原来还有B锁')
#                 # 释放B锁
#                 lockA.release()
#         # 释放A锁
#         lockB.release()
#
#
# if __name__ == '__main__':
#     t1 = MyThread1()
#     t2 = MyThread2()
#
#     t1.start()
#     t2.start()

