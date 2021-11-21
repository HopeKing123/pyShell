"""
情况二：获取Exception的错误原因
try:
    有可能出现多种异常
except:
    如果有异常执行的代码
except 异常类型2:
    pass
except Exception as err:
    print(err) ——————> error的内容就是错误原因.
"""


# 示例 情况二：
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
    except Exception as err:
        print('出错了!',err)


func()
print('-------->')