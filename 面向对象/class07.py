# __slots__变量：主要达到限制的目的，通过该变量来限制class实例能添加的属性
# 只允许对Student实例添加name和age属性
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的，除非在子类中也定义__slots__,子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class Student:
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# s.score = 99  # 绑定属性'socre' # 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
