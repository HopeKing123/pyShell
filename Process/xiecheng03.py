# -- coding: utf-8 --
# 协程爬虫案例

# import requests
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def download(path):
    # 下载路径资源
    response = urllib.request.urlopen(path)
    # 读response下载的资源
    content = response.read()
    # 打印
    print('下载了{}的数据,长度:{}'.format(path, len(content)))


if __name__ == '__main__':
    urls = ['http://www.163.com', 'http://www.qq.com', 'http://www.baidu.com']
    # 创建一个greenlet对象传入相应参数，并允许。
    # spawn参数(function, *args, **kwargs)
    g1 = gevent.spawn(download,urls[0])
    g2 = gevent.spawn(download,urls[1])
    g3 = gevent.spawn(download,urls[2])

    g1.join()
    g2.join()
    g3.join()

"""
分布式进程帮助文档：
    https://www.liaoxuefeng.com/wiki/1016959663602400/1017631559645600
"""