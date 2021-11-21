# 递归函数：函数自己调用自己
# 递归函数消耗资源较大，非特殊情况不建议使用
"""
递归函数的特点
1. 递归函数必须要有终点
2. 递归函数必须要有入口
3. 函数必须自己调用自己
"""


# 示例和
def sum(x):
    if x == 0:
        return 0    # 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10  return返回之前计算的值
    else:
        return x + sum(x - 1)


result = sum(10)
print(result)


# 求1-100的累加和
def fn(n):
    if n == 100:
        return 100
    else:
        return n + fn(n + 1)


result = fn(1)
print(result)
