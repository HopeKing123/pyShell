# 用户发表文章,创建用户对象

# 绝对路径导入包下模块中的类,基于项目来进行查找包
from 模块和包.user.models import User
from 模块和包.article.models import Article

# 调用user包模块下的类方法
user = User('admin', '123456')  # user就是通过导入User类创建的
user.show()

#
# 发表文章，文章对象
article = Article('西游记', '吴承恩')
user.publish_article(article)  # 这里传入的的参数为article对象参数

# 调用外部的module进行运算
from 模块和包.模块.module import add

list1 = [1, 4, 6, 8, 9]
a = add(*list1)
print(a)

# 相对路径导入模块中的类,相对路径会出现没有父包的问题，建议使用绝对路径
# from .models import User

