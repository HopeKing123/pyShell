# -- coding: utf-8 --
# 线程
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

"""
import time, threading


# 线程创建
# 模拟使用线程实现图片下载
def download(n):
    # 图片列表
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    # 循环图片列表
    for image in images:
        print('正在下载: ', image)
        # 休眠模拟正在下载图片
        time.sleep(n)
        print('下载{}成功！'.format(image))


# 模拟使用线程实现听音乐
def listenMusic(m):
    musics = ['晴天', '龙卷风', '珊瑚海']
    for music in musics:
        # 若线程在执行过程中休眠则会将CPU的执行权让出（抢占资源），由其他线程继续执行，休眠结束则等待其他线程执行完成后，继续执行。（休眠就相当于阻塞）
        time.sleep(m)
        print('正在听周杰伦的{}歌曲'.format(music))


# 主进程(主进程先执行，然后线程在执行)
if __name__ == '__main__':
    # 创建线程(线程)，模拟下载图片
    # 参数(self, group=None, target=None, name=None,args=(), kwargs=None, *, daemon=None)
    t1 = threading.Thread(target=download, name='线程一', args=(1,))
    # 启动线程
    # t1.start()
    # 线程模拟听音乐
    t2 = threading.Thread(target=listenMusic, name='线程二', args=(1,))
    # 启动线程
    # t2.start()


# 创建线程
"""
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
主线程实例的名字叫MainThread，子线程的名字在创建时指定，用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
"""


def loop():
    # 2.打印正在运行的子线程(LoopThread)
    print('thread %s is running...' % threading.current_thread().name)
    # 变量
    n = 0
    # 判断条件循环
    while n < 5:
        n = n + 1
        # 打印子进程,及条件循环
        print('thread %s >>> %s ' % (threading.current_thread().name, n))
        # 休眠
        time.sleep(1)
    # 打印子线程运行结束
    print('thread %s ended.' % threading.current_thread().name)


# 1.打印正在运行的主线程(MainThread)
print('thread %s is running....' % threading.current_thread().name)
# 创建线程,指定目标函数及线程名称
t = threading.Thread(target=loop, name='LoopThread')
# 启动线程
t.start()
# 等待线程运行结束后，再运行主线程
t.join()
# 打印主线程运行结束
print('thread %s ended.' % threading.current_thread().name)

