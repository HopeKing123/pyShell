"""
情况三： （try与else）
try:
    有可能出现多种异常
except 类型1:
    如果有异常执行的代码
else：
    如果try中没有发生异常则进入的代码

注意：如果使用else则在try代码中不能出现return，否则会终止else代码无法执行
"""


# 示例 情况三:
def func():
    try:
        n1 = int(input("输入数字："))
        print(n1)
        # return 1
    except ValueError:
        print('必须是数字....')
    else:
        print("数字输入完毕!")    # 没有异常才会执行的代码块


# 调用函数
func()