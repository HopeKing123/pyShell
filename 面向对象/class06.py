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

stu = Student('wangwu', computer, book) # 借取神墓书籍

# 看借了那些书
stu.show_book()

# 再次借书
book1 = Book('完美世界', '辰东', 8)
stu.borrow_book(book1)
print('-------------')
# 再次查看借了哪些书
stu.show_book()

# 继承和多态
# class Animal:
#     def run(self):
#         print('Animal is running...')
#
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')
#
#
# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')
#
#
# # 子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run().
# dog = Dog()
# dog.run()
#
# cat = Cat()
# cat.run()
#
#
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
# run_twice(Tortoise())
