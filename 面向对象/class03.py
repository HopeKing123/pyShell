# 学习网址：http://c.biancheng.net/view/4552.html
"""类方法和静态方法
内置类属性：实例属性 and 公有类属性及私有类属性
类中的方法(动作) 种类：普通方法、类方法、静态方法、魔术方法

类方法特点：
    1.定义需要依赖装饰器@classmethod
    2.类方法中的参数不是一个对象，而是当前类
    3.类方法只能使用类属性，不可使用对象属性.
    4.类方法不可以直接调用普通方法，因为在类方法中没有对象.
    5.加载时机在没有创建时就已经加载了
类方法的作用：
    只能访问类属性和类方法，所以可以在对象创建之前，若需要完成一些功能时就可以使用类方法。

静态方法的特点：
    1.定义需要依赖装饰器@staticmethod
    2.静态方法是无需传递参数的(self,cls)
    3.静态方法也只能访问类的属性和方法，而对象的是无法访问的
    4.加载时机同类方法

类方法和静态方法的区别
不同之处：
    1.装饰器不同
    2.参数不同
相同之处：
    1.只能访问类的属性和方法，对象的是无法访问的
    2.都可以通过类名调用访问
    3.都可以在创建对象之前使用，因为不依赖于对象

普通方法与两者的区别：
    1.没有装饰器
    2.普通方法永远是要依赖于对象，因为每个普通方法都有一个self
    3.只有创建了对象才可以调用普通方法，否则无法调用

"""


##############################################
# 普通方法
class test1:
    # 初始化对象属性
    def __init__(self, hero, skill):
        self.hero = hero
        self.skill = skill

    # 方法;动作
    def alliance(self):
        print('英雄叫做{},技能为{}'.format(self.hero, self.skill))


a = test1('男枪', '炸弹')
a.alliance()


##############################################
# 类方法 @classmethod
class CLanguage:
    # 类构造方法，定义公有对象属性
    def __init__(self):
        self.name = 'python'
        self.add = 'https://python.org'

    # 定义类方法
    @classmethod
    def info(cls):
        print('正在调用类方法', cls)


# 使用类名直接调用类方法
CLanguage.info()
# 使用类对象调用类方法
clang = CLanguage()
clang.info()


##############################################
# 私有化属性类
class Student:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 调用私有化属性
# bart = Student('Bart', 'male')
# print(bart._Student__name)


##############################################
# 静态方法@staticmethod
class CLanguage1:
    @staticmethod
    def info(name, add):
        print(name, add)


# 使用类名直接调用静态方法
CLanguage1.info('python', 'https://python.org')
# 使用类对象调用静态方法
clang = CLanguage1
clang.info('python', 'https://python.org')

##############################################
# 魔术方法 __new__


##############################################
# 魔术方法 __call__


##############################################
# 魔术方法 __del__


##############################################
# 魔术方法 __str__


"""
python内置参数：
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
"""


class Employee:
    """所有员工的基类"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount = + 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


print('Employee.__doc__:', Employee.__doc__)
print('Employee.__name__:', Employee.__name__)
print('Employee.__module__:', Employee.__module__)
print('Employee.__bases__:', Employee.__bases__)
print('Employee.__dict__:', Employee.__dict__)
