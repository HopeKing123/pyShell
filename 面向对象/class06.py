"""
has a：一个类中使用率另外一种自定义的类型
is a：继承关系，如果类中不定义__init__,调用父类的super class的__init__
      如果类继承父类也需要定义自己的__init__,就需要在当前类的__init__调用一下父类__init__
调用父类的__init__
    super().__init__(参数)
    super(类名，对象).__init__(参数)
默认搜索规则：先找当前类，再去找父类。父类提供的方法不能满足子类的需求，就需要在子类中定义一个同名的方法，这种行为：重写
"""
# has a
import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def get_time(self,road): # road = r
        ran_time = random.randint(1,10)
        # 数据格式化,在Car类中使用road类
        msg = '{}品牌的车在{}上以{}速度行驶{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的车，速度:{}'.format(self.brand,self.speed)


# 对象
r = Road('京藏高速',12000)
audi = Car('奥迪',120)
print(audi)
# 对象
audi.get_time(r)



# 继承和多态
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


def run_twice(animal):
    animal.run()
    animal.run()


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running ')


run_twice(Tortoise())
