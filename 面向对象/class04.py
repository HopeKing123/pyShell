# 魔术方法是在特定时刻自动触发
# https://www.cnblogs.com/zhangboblogs/p/7860929.html
# 魔术方法 __new__
"""
__init__：初始化魔术方法(构造)
触发时机：初始化对象时触发(不是实例化触发，但和实例化在一个操作中)，并且依赖于__new__
__new__：实例化魔术方法
触发时机：在实例化时触发（开辟空间）
    特点：
        1.若类中存在new，则会先加载new方法然后在执行init
"""
import sys


class Person:
    # 对象实例初始化
    def __init__(self, name):
        print("——————> init", self)
        self.name = name

    # 重写父的__new__方法,会返回None
    def __new__(cls, name):  # __new__ 向内存要空间 ---> 地址
        print("——————> new")
        # 继承父类__new__方法,python3__new__不需要传输参数
        position = super(Person, cls).__new__(cls)  # 申请内存开辟空间，然后return给init初始化
        print(position)
        return position  # return给对象，再由对象扔给init


p = Person('jack')
print(p)


# 魔术方法 __call__
"""
__call__：调用对象的魔术方法
触发时机：将对象当作函数调用时触发对象
参数：至少一个self接收对象，其余根据调用时参数决定
"""


class Person1:
    # 对象实例初始化
    def __init__(self, name):
        print("——————> init")
        self.name = name

    # 把对象当作函数使用时重写__call__即可
    def __call__(self, *args, **kwargs):
        print('------> call')


p1 = Person1('nice')
print(p1.name)
# 函数形式调用
p1()


# 魔术方法 __del__
"""
__del__：析构魔术方法
触发时机：当对象没有用(没有任何变量引用)的时候被触发。
        就是定义在对象销毁之前，需要做的某些操作。
参数：一个self参数

del特点：
    1. 对象赋值
    2. 删除地址的引用
    3. sys模块中getrefcount方法可以查看地址引用的次数
    4. 当一块空间没有任何引用次数时就会默认调用__del__方法,回收所有在本次执行过程中使用的空间，进行垃圾回收

程序结束前对象的引用还存在，则程序最后调用__del__;反之，则在之前调用
"""


class Person2:
    def __init__(self, name):
        self.name = name

    # 只要定义了__del_-方法，运行结束后就会执行del。
    def __del__(self):
        print('----del----')


# 对象赋值
p2 = Person2('bom')
a = p2
b = p2
print(a.name)
print(b.name)

# 删除地址引用
del b
print("删除b后打印:", p2.name)
del a
print("删除a后打印:", p2.name)

# 查看地址引用次数
print(sys.getrefcount(p2))


# 魔术方法 __str__
"""
__str__：将打印的地址信息，转换位面向开发可视化读取内容
触发条件：当打印对象名时自动触发去调用__str__里面的内容
参数：一个self
注意：需要在__str__方法中添加return，return后面内容就是打印对象内容
"""


class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "姓名是：" + self.name + "年龄：" + str(self.age)


p3 = Person3('tom', 18)
print(p3)

p4 = Person3('jack', 22)
print(p4)


"""
常用的魔术方法：
    __init__
    __str__
"""