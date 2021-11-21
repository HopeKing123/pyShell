# 装饰器付款
# 需求用户需要登陆才能进行服务，若没有登陆则跳转到登陆函数
import time

islogin = False  # 默认没有登陆


def login():
    username = input("请输入你的用户名: ")
    password = input("请输出你的密码： ")
    if username == 'admin' and password == '123456':
        return True
    else:
        return False


# 定义装饰器，进行付款验证
def login_required(func):
    def warpper(*args,**kwargs):
        global islogin
        print("--------付款--------")
        # 验证用户是否登陆
        if islogin:
            func(*args,**kwargs)
        else:
            # 跳转到登陆页面
            print("用户没有登陆，不能付款!")
            islogin = login()
            print('result',islogin)
    return warpper


@login_required
def pay(money):
    print("正在付款，付款金额是{}元".format(money))
    print("付款中...")
    time.sleep(2)
    print("付款完成!")


pay(10000)
pay(8000)