# 模块
"""
在python中，模块是代码组织的一种方式，把功能相近的函数放到一个文件中,一个文件(.py)就是一个模块(module)
- 提高代码的可复用，可维护性.一个模块编写完成后，可以很方便的在其他项目中导入
- 解决了命名冲突，不同模块中相同的命名不会冲突
模块分为：自定义模块，内置模块，第三方模块

导入模块：
1. import 模块名
    模块名.变量  模块名.函数  模块名.类
2. from 模块名 import 变量 | 函数 | 类
    在代码中可以直接使用变量，函数，类
3. from 模块名 import *
    导入该模块中所有的内容

4. 在模块中使用__all__ = ['']可以限制允许*通配符所导入的内容
5. 无论是import还是from的形式，都会将模块内容进行加载
若不希望其进行调用，就会使用__name__
    if __name == '__main__' 判断__name__等不等于__main__,等于则执行，不等于则不执行
        test()
__name__：在自己的模块里面__name__叫：__main__,如果在其他模块中通过导入的方式调用的话：__name__: 模块名

创建自己模块时，要注意：
模块名要遵循Python变量命名规范，不要使用中文，特殊字符
模块名不要与系统模块冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块

先加载后调用
"""

# 导入自己模块的第一种方式
import module

# 求和
list1 = [4, 3, 5, 7, 8, 9]

# 使用模块中的函数，模块名.变量 模块名.函数 模块名.类
result = module.add(*list1)
print(result)

# 使用模块中的变量
print(module.number)

# 使用模块中的类
mod = module.Module(99)
mod.test()

# 使用模块中类的类方法
module.Module.test1()

print('-------------------------------')
# 模块导入的第二种方式,导入其中一部分
from module import add,number,Module
# 导入所有
from module import *
result = add(*list1)
print(result)

sum = result + number
print(sum)

m = Module(77)
m.test()

"""
注意：在大型python项目中，需要很多python文件，由于架构不当，可能会出现模块之间的相互导入，应该避免出现这种情况。这种被称为"模块循环导入"
例如：
    A: 模块
        def test():
            f()
    B: 模块
        def f():
            test()
解决方法：
    1.重新架构，不推荐
    2.将导入的语句，放在函数里面
    3.把导入语句放到模块的最后
"""
























