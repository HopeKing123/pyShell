# 子进程
"""
很多时候，子进程并不是自身，而是一个外部进程(对外)。我们创建了子进程后，还需要控制子进程的输入和输出。
subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
"""

# 输出
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# 输入
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('GBK'))
# print('Exit code: ', p.returncode)


# 进程间的通信

"""
Process之间肯定是需要通信的，操作系统提了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来 交换数据。
"""
from multiprocessing import Process, Queue
import time


# 实现进程之间通信，模拟使用进程通信实现图片下载
def download(q):
    # 图片列表
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    # 循环图片列表
    for image in images:
        print('正在下载: ', image)
        # 休眠模拟正在下载图片
        time.sleep(0.5)
        # put(阻塞)：写数据,timeout参数表示若超时则抛出异常(把image写入自定义的Queue队列当中)
        q.put(image)


# 获取文件函数
def getfile(q):
    while True:
        # timeout参数超时会抛出异常，使用try进行异常处理
        try:
            # get(阻塞)：获取数据,timeout参数表示若超时则抛出异常(从Queue队列当中取值)
            file = q.get(timeout=2)
            # 模拟保存成功
            print('{}保存成功！'.format(file))
        except:
            # 触发异常就终止循环代码
            break


if __name__ == '__main__':
    # 定义Queue队列进行交换数据
    q = Queue(5)
    # target传入目标函数，args传入可变参数q(Queue)队列，并将该参数传给函数的自定义参数.
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))
    # 启动
    p1.start()
    # join()方法可以等待子进程结束后再继续往下运行，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p1.join()

    p2.start()
    p2.join()
    # 最后打印主进程
    print('图片下载完成......')

"""
队列参数：
put_nowait(非阻塞)：put_nowait表示没有要写入的值不阻塞，但会抛异常。可能存在数据写入丢失
get_nowait(非阻塞)：get_nowait表示取不到值不阻塞，但会抛异常。异步处理使用。
full：判断队列是否满
empty：判断是否为空
"""
"""
帮助文档：
    https://www.cnblogs.com/paulwhw/articles/10723887.html
"""