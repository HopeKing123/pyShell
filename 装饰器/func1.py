#装饰器

import time


def descrate(func):
    def warpper():
        print("校验中....")
        time.sleep(2)
        print("校验完成....")
        func()
    return warpper


# descrate = f1     f1 = warpper

@descrate
def f1():
    print("----------f1")


def f2():
    print("----------f2")


f1()
f2()
