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
