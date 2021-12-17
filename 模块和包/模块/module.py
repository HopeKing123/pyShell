# 自定义自己的运算模块
# 在模块中使用__all__ = ['']可以限制允许*通配符所导入的内容
__all__ = ['add', 'number', 'Module']

# 变量
number = 100
name = 'module'


# 函数

def add(*args):
    if len(args) > 1:
        sum = 0
        for i in args:
            sum += i
        return sum
    else:
        print("至少传入两个参数...")
        return 0


def minus(*args):
    if len(args) > 1:
        m = 0
        for i in args:
            m -= i
        return m
    else:
        print("至少传入两个参数...")
        return 0


def multiply(*args):
    pass


def divide(*args):
    pass


# 类

class Module:

    def __init__(self, num):
        self.num = num

    def test(self):
        print("正在使用Module进行运算...")

    @classmethod
    def test1(cls):
        print('---Module中类方法')


# 函数
def test():
    print("正在测试...")


# 无论是import还是from的形式，都会将模块内容进行加载，所以会执行函数调用
# test()

# 若不希望其进行调用，使用__name__进行判断
if __name__ == '__main__':
    test()
