# 写文件

"""
stream = open(r'I:\p1\a.txt','w')
mode 是 'w' 表示写操作

方法：
     write(内容)  每次都会将原来的内容清空，然后写当前的内容
     writelines(Iterable)   可迭代，换行加\n

如果mode='a'  内容会被追加到原有内容上


"""
stream = open(r'I:\p1\a.txt','a')

s = """
你好！
    这里第二维度之上的第四维度
        创建者：王占彪
"""
result = stream.write('hello')  # 会覆盖原有内容
# result = stream.write(s)
print(result)
stream.write('龙五')  # 指针光标在最后一位

# 写行，换行加\n
stream.writelines(['第六维度\n','第七维度\n','第八维度\n'])
# a 追加
stream.write("第八点五维度\n")
stream.write("第九维度\n")

stream.close()

