# __slots__变量：主要达到限制的目的，通过该变量来限制class实例能添加的属性
# 只允许对Student实例添加name和age属性
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的，除非在子类中也定义__slots__,子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class Student:
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# s.score = 99  # 绑定属性'socre' # 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

"""
__repr__：返回程序开发着看到的字符串，
__str__：返回用户看到的字符串
若直接调用变量而不是print，变量首先调用的是__repr__,而不是__str__,解决办法就是在定义一个__repr__.
"""


class Student1:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student object (name=%s)" % self.name

    __repr__ = __str__


wangwu = Student1('wangwu')

"""
__iter__方法
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环

__getitem__方法
可以像list一样按照下标取出元素
"""


# __getattr__方法：动态返回一个属性

class Student3:
    def __init__(self):
        self.name = "Michael"

    def __getattr__(self, attr):
        if attr == 'socre':
            return 'yes'


s = Student3()
var = s.score
print(var)


# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
# 注意，任何调用如s.score都会返回None,因为定义的__getattr__默认返回None值,
# 利用__getattr__动态模拟REST API.
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


chain = Chain().status.user.timeline.list
print(chain)

# callable判断一个对象是否是“可调用”对象。
print(callable(Student))
print(callable(Student1))
print(callable(Student3))


"""
枚举类：可迭代的
@unique装饰器可以帮助我们检查保证没有重复值。
"""
# 定义枚举类型的class类型，通过Enum类实现这个功能
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 访问枚举类型的方法：
# 可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # value属性则是自动赋给成员的int常量，默认从1开始计数。

day1 = Month.Feb
print(day1.value)

print(Month['Apr'])
print(Month['Apr'].value)

print(day1 == Month.Jan)
print(day1 == Month.Apr)
print(Month(1))

# 枚举练习：
from enum import Enum, unique


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

"""
type()函数可以差查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello
type()函数既可以返回一个对象的类型，又可以创建出新的类型.
比如：通过type()函数创建出Hello类，而无需通过class Hello(object)..的定义
"""


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

"""
要创建一个class对象，type()函数依次传入3个参数：
class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

静态语言与动态语言最大的区别在于：静态语言必须构造源代码字符串再调用编译器
"""


"""
元类：
metaclass：动态创建类
一般用于ORM对象-关系映射,就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
"""


# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
# metaclass是类的模板，所以必须从"type"类派生“：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return  type.__new__(cls, name, bases, attrs)


# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass
class MyList(list, metaclass=ListMetaclass):
    pass

"""
当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
__new__()方法接收到的参数依次是：
    当前准备创建的类的对象；
    类的名字；
    类继承的父类集合；
    类的方法集合。
"""
L = MyList()
L.add(1)
print(L)











