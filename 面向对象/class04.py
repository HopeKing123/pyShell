# 魔术方法 __new__
"""
__init__：初始化魔术方法
触发时机：初始化对象时触发(不是实例化触发，但和实例化在一个操作中)，并且依赖于__new__
__new__：实例化魔术方法
触发时机：在实例化时触发

特点：
    1.若类中存在new，则会先加载new方法然后在执行init
"""


class Person:
    def __init__(self, name):
        print("——————> init")
        self.name = name

    # 重写了父的__new__方法,会返回None
    def __new__(cls, name): # __new__ 向内存要空间 ---> 地址
        print("——————> new")
        # 继承父类__new__方法,python3__new__不需要传输参数
        return super(Person,cls).__new__(cls)   # 申请内存开辟空间，然后return给init初始化


p = Person('jack')


# 魔术方法 __call__
"""

"""


# 魔术方法 __del__
"""

"""


# 魔术方法 __str__
"""

"""


