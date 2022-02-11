# 进程池 非阻塞式
"""
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态生成多个进程
但如果是上百甚至上千个目标,手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool时，如果池还没有满，那么就会创建一个新的进程用来指向该请求，
但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来执行。

Pool进程池中的子进程与主进程共存亡，主进程若执行完退出，子进程则也不会再继续执行

进程池模式
阻塞式：添加一个执行一个任务，如果一个任务不结束另一个任务就进不来。
非阻塞式：全部添加到队列中，立刻返回，并没有等待其他的进程执行完毕，但是回调函数是等待任务完成之后才回调。
"""
import time
from multiprocessing import Pool
import os
# 非阻塞式进程
from random import random


def task(task_name):
    print('开始做{}任务！'.format(task_name), '当前进程PID: ', os.getpid())
    # 启动时间
    start = time.time()
    # sleep休眠模拟任务执行过程
    time.sleep(random() * 2)
    # 结束时间
    end = time.time()
    # print('完成任务:{},用时: {}'.format(task_name,(end - start)), '当前进程PID: ', os.getpid())
    # 将结果抛出去
    return '完成任务:{},用时: {}'.format(task_name, (end - start)), '当前进程PID: ', os.getpid()


# 存放task函数return出来的结果
container = []


# 接收并将task函数return出来的结果添加到container列表当中
def callback_func(n):
    container.append(n)


if __name__ == '__main__':
    # 创建5个进程池进程
    pool = Pool(5)

    # 创建任务列表
    tasks = ['每日备份', '日志筛选', '日志分析', '热点记录', '分发奖励', '日志归档']
    # 循环任务列表
    for i in tasks:
        # 调用进程池，apply_async表示非阻塞式模式,异步执行参数
        # 参数(self, func, args=(), kwds={}, callback=None,error_callback=None)
        pool.apply_async(task, args=(i,),
                         callback=callback_func)  # callback回调callback_func函数,将task函数return出来的值添加到container容器中

    # join()方法可以等待子进程结束后再继续往下运行，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    pool.close()  # 添加任务结束
    pool.join()

    for c in container:
        print(c)
    print('今日任务结束!')
# 请注意输入结果，任务'每日备份', '日志筛选', '日志分析', '热点记录', '分发奖励'是立刻执行的,而'日志归档'要等待前面某个任务完成后才执行，这是因为Pool进程池的默认大小在我电脑上是5，因此最多执行5个进程。
# Pool的默认大小式CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。
