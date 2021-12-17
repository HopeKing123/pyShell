"""
设计模式：
创建型模式
    1.单例模式
    2.工厂模式
    3.建造者模式
    4.原型模式
结构型模式
    1.适配器模式
    2.修饰器模式
    3.外观模式
    4.享元模式
    5.模型-视图-控制器模式
    6.代理模式
行为型模式
    1.责任链模式
    2.命令模式
    3.解释器模式
    4.观察者模式
    5.状态模式
    6.策略模式
    7.模板模式
"""

"""
单例模式：外界使用的是同一个地址空间.对内存进一步优化，

继承父类的方法：
    super().__init___
    return object.__init__
    
定义私有化属性__instance不被外界修改，重写父类的__new__方法，判断私有化属性__instance的值是否为None，
若为None则继承父类的__new__为__instance开辟空间然后return出去。若__instance不为空则直接return __instance
"""


class Singletion:
    # 私有化   单例的地址存在于__instance
    __instance = None

    # 重写__new__
    def __new__(cls):   # 开辟空间
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance   # return给父类的__init__,__init__再扔给实例
        else:
            return cls.__instance   # return给父类的__init__，__init__再扔给实例


s = Singletion()
s1 = Singletion()
print(s)
print(s1)
