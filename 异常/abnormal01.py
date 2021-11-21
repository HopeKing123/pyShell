# 异常处理
# 在代码编写的情况下无法判断是否有异常，只有在程序运行时才会抛出异常
"""
格式：
try:
    可能出现异常的代码
except 异常类型1:
    如果有异常执行的代码
[finally:
    无论是否存在异常都会被执行的代码]
"""


# 示例：
# def func():
#     try:
#         n1 = int(input("输入第一个数字："))
#         n2 = int(input("输入第二个数字："))
#
#         # 运算
#         per = input('输入运算符号(+ - * /):')
#
#         result = 0
#         if per == '+':
#             result = n1 + n2
#         elif per == '-':
#             result = n1 - n2
#         elif per == '*':
#             result = n1 * n2
#         elif per == '/':
#             result = n1 / n2
#         else:
#             print('符号输入有误！')
#         print('结果是：', result)
#     except ZeroDivisionError:
#         print('除数不能为零')
#     except ValueError:
#         print('必须输入数字')
#
#
# func()
# print('-------->')


"""
异常中存在多种情况：
情况一：
try:
    有可能出现多种异常
except 异常类型1:
    如果有异常执行的代码
except 异常类型2:
    pass
except Exception:
    pass

定义的多种异常类型都属于Except父类的子类，若在异常抛出过程中，无法确定err是什么类型的可以直接使用Except父类
如果是多个except,异常类型的的顺序需要注意,最大的Exception要放最后。放前面的话后面即使由符合的异常也无法将无法抛出！
"""


def func():
    try:
        n1 = int(input("输入第一个数字："))
        n2 = int(input("输入第二个数字："))

        # 运算
        per = input('输入运算符号(+ - * /):')

        result = 0
        if per == '+':
            result = n1 + n2
        elif per == '-':
            result = n1 - n2
        elif per == '*':
            result = n1 * n2
        elif per == '/':
            result = n1 / n2
        else:
            print('符号输入有误！')
        print('结果是：', result)

        # 文件操作,读。若文件不存在会报错,然后在异常类型中进行比较，若有符合异常则抛出，若没有则抛出最后的Exception.
        with open(r'I:\p1\aa.txt') as wstream:
            print(wstream.read())
        # 文件操作,写
        # with open(r'I:\p1\aa.txt') as wstream:
        #     wstream.write("本次运算的结果为:{}".format(result))

    except ZeroDivisionError:
        print('除数不能为零')
    except ValueError:
        print('必须输入数字')
    except Exception:
        print('出错了!')


func()
print('-------->')
