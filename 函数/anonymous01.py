# 匿名函数:简化函数定义部分
# 格式：lambda 参数1，参数2... :运算

# 求和
s = lambda a, b: a + b
print(s)  # s就是函数function
result = s(1, 2)
print(result)


# 拆解开
#
# def func(a, b):
#     return a + b

# resul = func(1, 2)
# print(resul)


# 匿名函数作为参数
def func(x, y, z):
    print(x, y)
    print(z)
    s = z(x, y)
    print(s)


func(2, 5, lambda a, b: a + b)

# 字典
list2 = [{'a': 10, 'b': 21}, {'a': 23, 'b': 41}, {'a': 75, 'b': 12}, {'a': 25, 'b': 45}]
m = max(list2, key=lambda x: x['a'])
print('最大值是：', m)

# 类似于
c = max(list2, key=lambda x: x['a'])
print(c)

empty = []
empty2 = []
for i in list2:
    empty.append(i['a'])
    empty2.append(i['b'])
print("a:", + max(empty))
print("b:", + max(empty2))
