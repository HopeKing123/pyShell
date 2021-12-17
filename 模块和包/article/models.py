# 包
"""
包(Package)：用于解决不同人编写的模块名相同问题,
包含关系：项目>包>模块>类 函数 变量
举个例子，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。
现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如下目录存放：

mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py

引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，
也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：

mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py

文件www.py的模块名就是mycompany.web.www，两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils。
注意：自己创建模块时要注意命名，不能和Python自带的模块名称冲突。

"""


class Article:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show(self):
        print('发表文章名字：{}的作者是：{}'.format(self.author, self.name))


class Tag:
    def __init__(self,name):
        self.name = name
























