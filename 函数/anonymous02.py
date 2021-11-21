# 对列表中进行加减乘除操作适用于 map
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = map(lambda x: x + 2, list1)
print(list(result))
# lambda判断
func = lambda x: x if x % 2 == 0 else x + 1
result = func(5)
print(result)
# map对列表中的奇数进行加+1操作
result = map(lambda x: x if x % 2 == 0 else x + 1, list1)
print(list(result))
# 函数
for index, i in enumerate(list1):
    if i % 2 != 0:
        list1[index] = i + 1
print(list1)

# reduce:对可迭代列表中的元素进行加减乘除运算的函数，列表元组都可以
from functools import reduce

# 格式：reduce(function, sequence, initial=_initial_missing)
# reduce(函数,序列,初始值) 函数需要携带两个参数.应用在序列的每个item上,
tuple1 = (1, 3, 5, 7, 9)
result = reduce(lambda x, y: x + y, tuple1)
print(result)
# reduce的initial运用
tuple2 = (1,)
result = reduce(lambda x, y: x + y, tuple2, 10)
print(result)


# filter: 过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
list2 = [12, 15, 7, 23, 32, 68]
result = filter(lambda x: x > 20, list2)
print(list(result))


# 通过函数形式
def func(list2):
    empty = []
    for i in list2:
        if i > 20:
            empty.append(i)
    return empty


result = func(list2)
print(result)

# 案例：过滤出年龄最大的学生
students = [
    {"name":"tom","age": 21},
    {"name":"lucy","age": 54},
    {"name":"lily","age": 24},
    {"name":"mark","age": 61},
    {"name":"jack","age": 34},
    {"name":"steven","age": 18},
]
result = filter(lambda x:x['age'] > 20,students)
print(list(result))

# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#  sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。 倒叙将reverse=True
students = sorted(students,key=lambda x:x['age'],reverse=True)
print(students)

# 总结
# min,max,sorted函数会结合key的使用
