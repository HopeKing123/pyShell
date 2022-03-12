# 私有化：不想被外界随意的修改
# 封装：1.私有化属性 2.定义共有set和get方法
"""
特点：
    1.隐藏属性不被外界随意修改
    2.通过定义set及get进行修改获取
    3.获取具体的某个属性，使用get函数获取
"""


class Student:
    def __init__(self, name, age):
        # 私有化属性
        self.__name = name
        self.__age = age
        self.__score = 59

    # 定义公有set和get方法
    # set为了赋值
    def setAge(self, age):
        if age > 0 and age < 120:
            self.__age = age
        else:
            print("年龄不合法")

    # get为了取值
    def getAge(self):
        return self.__age

    # 定义修改名字，长度必须6位
    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print("名字不合法")

    def getName(self):
        return self.__name

    # 重写__str__返回内容
    def __str__(self):
        return '姓名:{}，年龄{},考试分数{}'.format(self.__name, self.__age, self.__score)


# 对象
lisi = Student('lisi', 20)
print(lisi)
# 修改年龄
lisi.setAge(24)
print(lisi)

# 对象
wangwu = Student('wangwu', 21)
print(wangwu)

# dir() 函数不带参数时,返回当前范围内的变量、方法和定义的类型列表;带参数时,返回参数的属性、方法列表。(不会返回私有属性)
print(dir(Student))

# 双下划线开头的实例变量不能直接访问__name,是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
print(wangwu._Student__name)  # 强烈建议不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。

# 举例：
# 开发中的私有化应用
"""
@property将私有化属性，伪装为公有属性
"""


class Student1:
    def __init__(self, name, age):
        # 私有化属性
        self.name = name
        self.__age = age

    # 通过装饰器伪装方法，把方法变成属性
    # 先有get
    @property
    def age(self):
        return self.__age

    # @property把方法变成属性之后，会创建另一个装饰器@age.setter
    # 通过调用上述get的age来绑定如下set的age动作，再用set，因为set依赖get
    @age.setter
    def age(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            print("年龄不合法")

    # 定义公有set和get方法
    # set为了赋值
    # def setAge(self, age):
    #     if age > 0 and age < 100:
    #         self.__age = age
    #     else:
    #         print("年龄不合法")
    #
    # # get为了取值
    # def getAge(self):
    #     return self.__age

    # 重写__str__返回内容
    def __str__(self):
        return '姓名:{}，年龄{}'.format(self.name, self.__age)


# 对象
s = Student1('zhangsan', 18)
print(s)

# 修改公有属性name
s.name = 'libai'
print(s.name)

# 私有化属性赋值
# s.setAge(30)
# print(s.getAge())

# 通过装饰器所调用的私有化属性
print(s.age)
# 通过装饰器所调用的私有化属性
s.age = 130
print(s.age)
