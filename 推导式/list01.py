# 列表推导式
# 旧列表 - 新列表
# 格式：[表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if 条件]

# 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else

# 过滤掉长度小于或等于3的人名
names = ['tom', 'lily', 'abc', 'jack', 'steven', 'bob', 'ha']

result = [name for name in names if len(name) > 3]
print(result)

# 类似于
"""
def func(names):
    newlist = []
    for name in names:
        if len(name) > 3:
        newlist.append(name)
    return newlist
func(names)
"""

# 将首字母大写
# 1、capitalize() 将字符串的首字母大写，其余字母小写
# 2、title() 将字符串中每个单词的首字母大写，其余字母小写，非字母后的第一个字母将转换为大写字母
# 3、upper()&lower() 全部单词大写或小写

result = [name.capitalize() for name in names if len(name) > 3]
print(result)

# 将1-100之间能被3整除，组成一个列表
result = [i for i in range(1, 101) if i % 3 == 0]
print(result)

# 求0-5之间的偶数，0-10之间的奇数 组成一个列表元组
# [(0,1),(0,2),(0,3)....]
result = [(i, j) for i in range(5) if i % 2 == 0 for j in range(10) if j % 2 != 0]
print(result)

# 类似于
# def func():
#     newlist=[]
#     for i in range(5): # 偶数
#         if i % 2 == 0:
#             for j in range(10): # 奇数
#                 if j % 2 != 0:
#                     newlist.append((i,j))
#     return newlist
#
# result = func()
# print(result)

# 取出3 6 9 5 并放入一个列表
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
result = [i[-1] for i in list1]
print(result)


# if推导式
dict1 = {'name':'tom','salary':5000}
dict2 = {'name':'lucy','salary':8000}
dict3 = {'name':'jack','salary':4500}
dict4 = {'name':'lily','salary':3000}

list1 = [dict1,dict2,dict3,dict4]


# if 薪资大于5000加200,低于等于5000加500
result = [employee['salary'] + 200 if employee['salary'] > 5000 else employee['salary'] + 500 for employee in list1]
print(result)

# 类似于
# result = []
# for employee in list1:
#     if employee['salary'] > 5000:
#         result.append(employee['salary'] + 200)
#     else:
#         result.append(employee['salary'] + 500)
#
# print(result)
