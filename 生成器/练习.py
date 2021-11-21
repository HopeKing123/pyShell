# 杨辉三角
"""
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1

前提：每行端点与结尾的数为1.
1.每个数等于它上方两数之和。
2.每行数字左右对称，由1开始逐渐变大。
3.第n行的数字有n项
4.前n行共[(1+n)n]/2个数。
5.前n行的m个数可表示为C(n-1,m-1),即为从n-1个不同元素中取m-1个元素的组合数。
6.第n行的第m个数和第n-m+1个数相等 ，为组合数性质之一。
7.每个数字等于上一行的左右两个数字之和。可用此性质写出整个杨辉三角。即第n+1行的第i个数等于第n行的第i-1个数和第i个数之和，这也是组合数的性质之一。即 C(n+1,i)=C(n,i)+C(n,i-1)。
"""


def triangles():
    L = [1]
    print(range(len(L)))    # range的第一个步长为0
    while True:
        yield L  # 生成器 return L + 暂停
        L = L + [0]  # [1,0]
        L = [L[i] + L[i - 1] for i in range(len(L))]  # i = 0

        # for i in range(len(L)):
        #     L = L + [0]
        #     L = L[i] + L[i - 1] # L = 1[0] + 1[0 - 1]


g = triangles()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
