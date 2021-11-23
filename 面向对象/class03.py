"""类方法和静态方法
内置类属性
类中的方法(动作)
种类：普通方法、类方法、静态方法、魔术方法
"""
"""
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
"""
# 学习网址：http://c.biancheng.net/view/4552.html

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


# 静态方法@staticmethod
class CLanguage1:
    @staticmethod
    def info(name, add):
        print(name, add)


# 使用类名直接调用静态方法
CLanguage1.info('python','https://python.org')
# 使用类对象调用静态方法
clang = CLanguage1
clang.info('python','https://python.org')

