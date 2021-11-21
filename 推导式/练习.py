# 练习一：
# 内建的isinstance函数可以判断一个变量是不是字符串
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i.lower() for i in L1 if isinstance(i, str)]
print(L2)


# 练习二：
# 内置enumerate函数可以把一个list变成索引-元素对.
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)

    max1 = L[0]

    min1 = L[0]

    for n in L: # [7,1]

        if max1 - n < 0:
            max1 = n

        if min1 - n > 0:
            min1 = n

    return min1, max1


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


# 练习三：
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    if s == '':
        return s
    if s[0] != ' ' and s[-1] != ' ':
        return s
    elif s[0] == ' ' and s[-1] == ' ':
        return s[2:-2]
    elif s[0] == ' ':
        return s[2:]
    elif s[-1] == ' ':
        return s[0:-2]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
