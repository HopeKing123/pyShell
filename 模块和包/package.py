# 包
"""
article
    /-models.py
    /-__init__.py
    /-...
user
    /-models.py
    /-__init__.py
    /-test.py

"""

# 使用包中模块中的User类
# 方法一：通过from来使用包里面的模块
from user import models

u = models.User('admin', '123456')
u.show()

# 方法二：通过from来使用包里面的模块的类
from user.models import User

u1 = User('wangwu', '123456')
u1.show()

from article.models import Article

a = Article('西游记', '吴承恩')
a.show()


# 包的__init__
"""
__init__.py:
当导入包的时候，默认调用__init__.py文件
作用:
    1.当导入包的时候，把一些初始化的函数，变量，类定义在__init__.py文件中
    2.此文件中函数，变量等的访问，只需要通过包名.函数既可访问.前提是导入包
    3.若通过from将包中的所以模块都导入(from 包 import 模块)，则需要在__init__.py文件中允许相应模块(__all__)
    
from 模块 import *:
表示可以使用模块里面的所有内容，如果没有定义__all__所有都可以访问，如果添加了__all__那么只有__all__=[] 列表中可以访问的

from 包 import *：
表示该包中内容(模块)是不能访问的，就需要在__init__.py文件中定义__all__=[] 列表中定义允许访问的模块
"""

# import user
# from user.models import User


# 导入包中所有模块,但是该包中的模块是不能访问的，需要在__init__中定义__all__允许访问相应的模块
from user import *

user = models.User('admin','123456')
user.show()









