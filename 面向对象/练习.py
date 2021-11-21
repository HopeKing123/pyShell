# 练习一：
# class Student:
#     def __init__(self, name, score):
#         # 属性
#         self.name = name
#         self.score = score
#
#     # 方法
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'


# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)


# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())

# 练习二：
# class Student:
#     # 类属性
#     name = 'lisi'
#     age = 2


# # 访问类方法
# lisi = Student()  # 创建lisi内存空间
# print(lisi.name)
# print(lisi.age)
#
# # 修改'age'属性
# lisi.age = 18  # 将修改后的属性写在lisi对象属性内存空间中,不会对类属性有影响
# print(lisi.age)
#
# # 修改'name'属性
# wangwu = Student()
# wangwu.name = 'wangwu'
# print(wangwu.name)


# 练习三：
# class Employee:
#     empCount = 0
#
#     def __init__(self, name, salary):
#         # 属性
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     # 方法
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     # 方法
#     def displayEmployee(self):
#         print("Name: ", self.name, ", Salary: ", self.salary)


# 对象
# emp1 = Employee("Zara", 2000)
# emp2 = Employee("Manni", 5000)
# 访问类方法
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)


# 练习四：
# 把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性
# class Student:
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self,gender):
#         self.__gender = gender
#
#
# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


# 私有化属性类
# class Student:
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
#
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self,gender):
#         self.__gender = gender
#
# 调用私有化属性
# bart = Student('Bart', 'male')
# print(bart._Student__name)

# 练习五：
# python内置类属性调用
# class Employee:
#     """所有员工的基类"""
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount = + 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name : ", self.name, ", Salary: ", self.salary)
#
#
# print('Employee.__doc__:', Employee.__doc__)
# print('Employee.__name__:', Employee.__name__)
# print('Employee.__module__:', Employee.__module__)
# print('Employee.__bases__:', Employee.__bases__)
# print('Employee.__dict__:', Employee.__dict__)

# 练习六 类方法
# class Person:
#     __age = 18
#
#     def show(self):
#         print('-------->', Person.__age)
#
#     @classmethod
#     def update_age(cls):
#         cls.__age = 20
#         print('-------->类方法')
#
#
# # 调用类方法
# Person.update_age()
# # 调用普通方法
# p = Person()
# p.show()


# 练习七 静态方法
class Person:
    __age = 18

    def __init__(self):
        self.name = 'jack'

    def show(self):
        print('-------->', Person.__age)

    # 类方法
    @classmethod
    def update_age(cls):
        cls.__age = 20
        print('-------->类方法')

    # 静态方法
    @staticmethod
    def test():
        print('------->静态方法')
        print(Person.__age)


# 调用类方法
Person.update_age()
Person.test()
# 调用普通方法
p = Person()
p.show()
