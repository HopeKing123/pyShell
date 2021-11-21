# 装饰器

def zhuang1(func):
    print("刷漆开始....")

    def warpper(*args, **kwargs):
        func()
        print("刷漆....")

    print('刷漆结束....')
    return warpper


def zhuang2(func):
    print("装修开始....")

    def warpper(*args, **kwargs):
        func()
        print("铺地板....")

    print("装修结束....")
    # return函数加()就是调用，不加()就是返回值
    return warpper


@zhuang2
@zhuang1
def house():
    print("毛胚房....")


house()
