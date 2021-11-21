# 定义生成器方式二：借助函数完成

"""
函数定义为生成器的步骤：
1.定义一个函数，函数中使用yield关键字
2.调用函数，接收调用的结果
3.得到的结果就是生成器
4. 借助于nex(), __next__得到生成器
"""


# 生成器
# 只要函数中出现了yield关键字，说明函数就不是函数，而是生成器。
# def func():
#     n = 0
#     while True:
#         n = +1
#         yield n  # 生成器，类似于 return n + 暂停


# 调用函数
# g = func()
# print(next(g))


# 菲波那切数 生成器
# 前两个数相加得出第三个数，就是菲波那切数
def fib(length):
    a, b = 0, 1
    n = 0

    while n < length:
        yield b     # 生成器
        a, b = b, a + b
        n += 1

    return '没有更多元素！！！'  # return就是在得到StopIteration后提示信息


g = fib(8)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
