"""
has a：一个类中使用率另外一种自定义的类型
is a：继承关系，如果类中不定义__init__,调用父类的super class的__init__
      如果类继承父类也需要定义自己的__init__,就需要在当前类的__init__调用一下父类__init__
调用父类的__init__
    super().__init__(参数)
    super(类名，对象).__init__(参数)
默认搜索规则：先找当前类，再去找父类。父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为：重写

知识点:
    1.理解 has a的关系
    2.类型：
        系统提供类型：str int list dict
        自定义类型：自定义的类
    3.
"""
# has a
import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):  # road = r
        ran_time = random.randint(1, 10)
        # 数据格式化,在Car类中使用road类
        msg = '{}品牌的车在{}上以{}速度行驶{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的车，速度:{}'.format(self.brand, self.speed)


# 对象
r = Road('京藏高速', 12000)
audi = Car('奥迪', 120)
print(audi)
# 对象
audi.get_time(r)


# has a 应用学生图书管理系统
# student book Computer
class Computer:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color

    def online(self):
        print("正在使用电脑上网......")

    def __str__(self):
        return self.brand + '---' + self.type + '---' + self.color


class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + '---' + self.author + '---' + str(self.number)


class Student:  # has a
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        # 列表存储书籍
        self.books = []
        # 将书籍append添加至列表中
        self.books.append(book)

    # 借取书籍
    # 若书籍已存在于列表当中则该书籍以及被借取过了，若不存在则添加至列表中，表示借取成功！
    def borrow_book(self, book):
        for book1 in self.books:
            if book1.bname == book.bname:
                print('已经借过了!')
                break
        else:
            # 添加至列表中
            self.books.append(book)
            print('{}本 借取成功！'.format(book))

    # 查询书籍调用Book类的bname
    def show_book(self):
        for book in self.books:  # book就是book对象
            print(book.bname)

    # 需要将object自定义类型强转str类型
    # 重写就是父类中的方法无法满足需求，在子类中自定义相同的方法就是重写
    def __str__(self):
        return self.name + '---' + str(self.computer) + '---' + str(self.books)


# 创建对象
computer = Computer('Mac', 'Mac pro 2018', 'grey')

book = Book('神墓', '辰东', 10)

stu = Student('wangwu', computer, book)  # 借取神墓书籍

# 看借了那些书
stu.show_book()

# 再次借书
book1 = Book('完美世界', '辰东', 8)
stu.borrow_book(book1)
print('-------------')
# 再次查看借了哪些书
stu.show_book()

####################################################################################
# 继承和多态
"""
1.只要创建对象底层就会调用__new__创建空间，然后__init__对象实例化。
2.继承的关系就是若子类中不存在相应的动作就会往上层父类中去找。
3.super()函数表示调用上层的父类
4.如果类继承父类也需要定义自己的__init__，就需要在当前类的__init__调用一下父类__init__
5.如何调用父类__init__:
    super().__init(参数)
    super(类名，对象).__init__(参数)
6.如果父类有eat(),子类也定义一个eat方法，默认搜索的原则：先找当前类，再去找父类  
7.父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法。这种行为：重写
8.子类的方法中也可以调用父类的方法
    super().方法名(参数)
"""


# 继承
# 父类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, *args, **kwargs):
        print(self.name + "正在吃饭...")

    def run(self, *args, **kwargs):
        print(self.name + "正在跑步...")


# 子类
class Student(Person):
    # 属性实例化
    def __init__(self, name, age, clazz):
        # 继承父类,将自己的name和age的值传给父类
        super().__init__(name, age)
        self.clazz = clazz

    def study(self, course):
        print("{}正在学习{}课程".format(self.name, course))

    # 导致阴影是因为父类没有参数，而子类有参
    def eat(self, foold):
        # 调用父类的方法
        super().eat()
        print(self.name + "吃的是{}".format(foold))


# 子类
class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager


# 子类
class Doctor(Person):
    def __init__(self, name, age, patients):
        # 判断属性是否属于Doctor类型
        super(Doctor, self).__init__(name, age)
        self.patients = patients


# 对象
s = Student('jack', 18, '2020')
s.run()
s.study('python基础')
s.eat('鲍鱼龙虾面')
# 对象
e = Employee('tom', 23, 10000, 'king')
# 对象
lists = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
d = Doctor('lucy', 30, lists)

# 继承应用案例
"""
编写一个简单的工资管理程序，系统可以管理以下四类人：工人(worker)、销售员(salesman)、经理(manager)、销售经理(salemanger)
所有员工都具有员工号、姓名、工资等属性，有设置姓名、获取姓名、获取员工号、计算工资等方法
    1) 工人：工人具有工作小时数和时薪的属性，工资计算方法为工作小时数*时薪
    2) 销售员：具有销售额和提成比例的属性，工资计算方法为销售额*提成比例
    3) 经理：具有固定月薪的属性，工资计算方法为固定月薪
    4) 销售经理：工资计算方法为销售额*提出比例+固定月薪
请根据以上要求设计合理的类，完成以下功能：
    1)添加所有类的人员  v
    2)计算月薪
    3)显示所有人的工资情况
"""


class System:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    # 设置姓名
    def Sname(self, name):
        self.name = name

    # 获取信息
    def __str__(self):
        msg = "工号为: {},姓名叫做：{},固定月工资：{}".format(self.id, self.name, self.salary)
        return msg

    # 基本工资工资
    def Csalary(self):
        return self.salary


# 工人
class Worker(System):
    def __init__(self, id, name, hours, hourly, salary):
        super(Worker, self).__init__(id, name, salary)
        self.hours = hours
        self.hourly = hourly

    # 工资计算方法为工作小时数*时薪
    # 重写父类工资方法
    def Csalary(self):
        money = self.hours * self.hourly
        self.salary += money
        return self.salary


# 销售员
class Salesman(System):
    def __init__(self, id, name, sales, ratio, salary):
        super(Salesman, self).__init__(id, name, salary)
        self.sales = sales
        self.ratio = ratio

    # 工资计算方法为销售额*提成比例
    def Csalary(self):
        money = self.sales * self.ratio
        self.salary += money
        return self.salary


# 经理
class Manager(System):
    def __init__(self, id, name, msalary, salary):
        super(Manager, self).__init__(id, name, salary)
        self.msalary = msalary

    # 工资计算方法为固定月薪
    def Csalary(self):
        money = self.msalary
        self.salary += money
        return self.salary


# 销售经理
class Salemanger(System):
    def __init__(self, id, name, sales, ratio, msalary, salary):
        super(Salemanger, self).__init__(id, name, salary)
        self.sales = sales
        self.ratio = ratio
        self.msalary = msalary

    # 工资计算方法为销售额*提出比例+固定月薪
    def Csalary(self):
        money = self.sales * self.ratio + self.msalary
        self.salary = + money
        return self.salary


# 工人对象
w = Worker('001', 'wangwu', 160, 100, 2000)
w = w.Csalary()
print("工资为：", w)

# 销售员对象
s = Salesman('002', 'lisi', 1500000, 0.03, 5000)
s = s.Csalary()
print('工资为：', s)

# 经理对象
m = Manager('003', 'zhangsan', 5000, 5000)
m = m.Csalary()
print('工资为：', m)

# 销售经理对象
sa = Salemanger('004', 'zhaosi', 1000000, 0.03, 50000, 25000)
sa = sa.Csalary()
print('工资为：', sa)


# 继承应用
class Animal:
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


# 子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run().
dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 多继承与搜索顺序
"""
python允许多继承
    def 子类(父类1，父类2,...)
        pass
        
如果父类中有相同名称方法，搜索顺序：
1.经典类(python2),深度优先，在python3环境中默认就是新式类。
    深度是一条线走到底再走另一条
2.新式类(python3),广度优先
    广度是按层次走
"""


# 多继承
class Base:
    def test(self):
        print("------> Base")


class A(Base):
    def test(self):
        print("------> AAA")


class B(Base):
    def test(self):
        print("------> BBB")


# 多继承
class C(Base):
    def test(self):
        print("------> CCC")


class D(A, B, C):
    pass


# 对象
d1 = D()
d1.test()

# 查看搜索顺序
import inspect

# getmro返回的是一个元组
print(inspect.getmro(D))
print(D.__mro__)


# 搜索顺序
# python3 从左至右，广度优先
class P1:
    def foo(self):
        print("p1.foo")

    def bar(self):
        print("p1.bar")


class P2:
    def foo(self):
        print("p2.foo")


class C1(P1, P2):
    pass


class C2(P1, P2):
    def bar(self):
        print("C2.bar")


class D(C1, C2):
    pass


# 对象
d2 = D()
d2.foo()
d2.bar()
print(D.__mro__)


# 多态
"""
多态是指一类事务有多种形态。
多态的好处就是，当我们传入Dog、Cat、Tortoise...时，只需要接收Person类型就可以了，因为Dog、Cat、Tortoise....都是Person类型。
按照Person类型进行操作即可。由于Person类型有run()方法，因此传入的任意类型，只要是Person类或者子类，就会自定调用实际类型的run()方法，这就是多态

对于一个变量，我们只需要知道它是Person类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Person、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，
这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则

若父类中存在私有化属性，则子类是无法直接继承父类的私有化属性

"""


# 人类
class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):
        # 多态
        if isinstance(pet, Cat):  # (object,type) type可以传入任意的类型，调用方只管调用即可
            print("{}喜欢养宠物：{}".format(self.name, pet.role))
        else:
            print("不是宠物类型")


# 宠物类
class Pet:
    role = "Pet"

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show(self):
        print("昵称：{}，年龄：{}".format(self.nickname, self.age))


# 猫类
class Cat(Pet):
    role = "猫"

    def catch_mouse(self):
        print("抓老鼠...")


# 狗类
class Dog(Pet):
    role = "狗"

    def watch_house(self):
        print("看家高手...")


# 虎类
class Tiger:
    def eat(self):
        print("太可怕了，可以吃人")


# 创建对象
cat = Cat("花花", 2)
dog = Dog("大黄", 4)
person = Person("李四")
person.feed_pet(cat)


# 多态
# 定义函数
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
#
# class Tortoise(Animal):
#     def run(self):
#         print('Tortoise is running ')
#
#
# # 调用函数
# run_twice(Tortoise())

"""
复习流程：
    1.__init__
    2.重写方法
    3.多继承
    4.多态
"""
