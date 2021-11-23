"""
面向过程：
把一个大象放进冰箱需要几步？
1.打开冰箱   # 对象
2.把大象放进去 # 对象
3.关闭冰箱  # 对象


面向对象：
上帝(程序员)
class类(人) instance实例(你，我，他) 你会有些属性(身高，年龄，体重) 你会有些技能(吃饭，泡妞)
__init__方法主要作用初始化你的属性，这些属性在上帝初始化你的时候就要赋予给你，比如zhangsan = Person(170，29，50)
这时上帝就把你创造出来了，也就是实例化了你。然后你到底有哪些技能呢，这就看有没有在类里面定义了，如果有定义泡妞的技能，那么你就可以调用泡妞的技能来泡妞，
代码：
class Person(object):
# 这里就是初始化你将要创建的实例的属性
    def __init__(self,hight,weight,age):
        self.hight = hight
        self.weight = weight
        self.age = age

# 定义你将要创建的实例所有用的技能
    def paoniu(self):
        print('你拥有泡妞的技能')

    def eat(self):
        print('you can eat')

# 开始创建实例
zhangsan=Person(170,50,29)
lisi = Person(175,100,30)

# 你的实例开始使用它的技能
zhangsan.paoniu()
lisi.eat()


面向对象关键词：
类：抽象的模板
对象：实例根据类创建出来的一个具体的"对象"，每个对象都拥有相同的方法，但各自的数据可能不同
属性：方法的特征
方法：与实例绑定的函数，与普通函数不同，方法可以直接访问实例的数据

面向对象的设计思想是抽象出class，根据class创建实例(instance)
"""


"""
格式：
# 所有的类名要求首字母大写，多个单词使用驼峰式命名
# 定义类是通过class关键字：
class Student([父类]):
    属性：特征
    方法：动作

定义好类之后，就可以根据Student类创建出Student类的实例，创建实例是通过类名+()实现的
bart = Student()

可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性
>>> bart.name = 'Bart Simpson'
>>> bart.name
'Bart Simpson'

在创建实例的时候，可以通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
代码：
class Student(object):

    def __init__(self, name, score):
        # 属性
        self.name = name
        self.score = score
        
注意到__init__方法的第一个参数永远是self，表示创建的实例(对象)本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

>>> bart = Student('Bart Simpson', 59)
>>> bart.name
'Bart Simpson'
>>> bart.score
59

类中函数和普通函数的区别：
类中定义的函数的第一个参数永远是实例变量self。并且，调用时不用传递该参数。除此之外和普通函数没有区别。
"""

"""
数据封装
在Student类中，每个实例拥有各自的name和score数据，我们可以直接在Student类的内部定义访问数据的函数，这样就把数据给封装起来了。
这些封装数据的函数和Student类本身是关联起来的，所以称之为类的方法。好处是可以增加新的方法

类属性和对象属性：
先从自己属性内存空间中找对应的方法，没有则从类属性内存空间中去找

"""


# 处理学生的成绩表
class Student:
    # __init__方法主要作用初始化你的对象属性
    def __init__(self, name, score):
        # 对象属性
        self.name = name
        self.score = score

        # 方法
    def print_score(self):
        print('%s: %s' % (self.name, self.score))


# 对象(对象属性)
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

# 访问类动作
bart.print_score()
lisa.print_score()

