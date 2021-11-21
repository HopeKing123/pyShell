"""
情况五：(raise)
raise:主动（手动）报出异常
def register():
    username = input('输入用户名：')
    if len(username) < 6:
        raise Exception('用户长度必须6位以上')
    else:
        print('输入的用户名是：'，username)
"""


# 示例 情况五：
def register():
    username = input('输入用户名：')
    if len(username) < 6:
        raise Exception('用户长度必须6位以上')   # 主动抛出异常
    else:
        print('输入的用户名是：', username)


try:
    register()
except Exception as err:
    print(err)
    print("注册失败！")
else:   # 没有发生异常则执行else
    print("注册成功!")
