# 可迭代的对象：1. 生成器 2.元组 列表 集合 字典
# https://www.cnblogs.com/xywq/p/7813915.html python迭代器 & __iter__方法

from collections.abc import Iterable

# 如何判断对象是否是可迭代的
list1 = [1, 4, 7, 8, 8]
f = isinstance(list1, Iterable)  # isinstance返回布尔值
print(f)    # True

# 判断生成器是否可迭代
g = (x + 1 for x in range(10))
f = isinstance(g, Iterable)
print(f)    # True

"""
迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束
迭代器只能往前不会退后。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

生成器是可迭代的，也是迭代器
list,dict,str是可迭代的，但不是迭代器,因为Iterator可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
实现了`__next__`方法的对象都可以被 next() 作用, 但如果该对象没有实现`__iter__`方法，则不是 Iterator类型。
"""
"""
生成器与迭代器：
只要能够用next()产生元素就是迭代器

生成器是迭代器中的一部分，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。

列表，元组，字典，集合可以借助iter转成迭代器。

"""

# 将列表list1转为可以迭代的
list1 = iter(list1)  # 通过iter()函数将可迭代的变成了一个迭代器
print(type(list1))
print(next(list1))
print(next(list1))
