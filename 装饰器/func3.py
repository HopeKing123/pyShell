# 装饰器3,装饰器携带参数
def floor(y):           # 第一层接收装饰器参数
    def renovation(func):   # 第二层接收函数   func == house
        def warpper(*args,**kwargs):    # 第三层接受函数实参 house == warpper
            func(*args,**kwargs)
            print("已经铺了{}块地板了...".format(y))    # 调用y
        return warpper  # house = warpper
    return renovation   # 返回结果 renovation返回结果给floor


@floor(10)
def house(x):
    print("这是我在{}年买的毛胚房...".format(x))


house("2021")


@floor(100)
def street():
    print("新街口街道需要铺地板...")


street()




