# 图书馆管理系统
import os, re



# 用户注册功能
def register():
    username = input("注册用户：")
    password = input("输入密码：")
    # 验证密码
    repassword = input("再次确认密码：")

    if password == repassword:
        # 保存信息
        with open(r'I:\books\users.txt', 'a') as wstream:
            wstream.write('\n{} {}\n'.format(username, password))

        print('用户注册成功!')
    else:
        print('密码不一致！')


# 调用函数
# register()


# 用户登陆功能
def login():
    username = input("输入用户名：")
    password = input("输入密码：")

    # 用户匹配判断
    if username and password:
        with open(r'I:\books\users.txt', 'r') as rstream:
            while True:
                user = rstream.readline()

                # 退出条件1
                if not user:
                    print('用户名输入错误或未注册！')
                    register()
                    break

                input_user = '{} {}\n'.format(username, password)

                # 退出条件2
                if user == input_user:
                    print('用户登陆成功!')
                    break


# login()

# 列出书籍功能
def show_books():
    print('-----------图书馆里面的图书有：------------')

    with open(r'I:\books\books.txt', 'r') as rstream:
        books = rstream.readlines()
        for book in books:
            print(book, end='')


# 调用函数
# show_books()


# 用户借书功能
# 用户首先登陆图书管理系统然后进行借书，此登陆分为两个阶段，若用户所登陆的账户没有注册则跳转到注册功能，若用户已注册则跳转到登陆功能。
# 用户登陆成功后，将展示图使馆中的书籍，然后由用户自行进行选择所需要借的书籍，并将其记录在user_books文本中后续还书进行调用。
def borrow():
    login()
    show_books()
    username = input("\n请输入你的姓名：")
    print('--------------进入借书功能------------------')
    user1_books = input("请选择你要借取的书籍：")

    # 若书籍未借出则借取成功，若书籍已借出则返回信息
    if username and user1_books:
        user_books = username + ':' + user1_books

        while True:
            with open(r'I:\books\user_book.txt', 'r', encoding='gbk') as rstream:
                books_user = rstream.read().splitlines()

                for i in books_user:
                    Separate = i.split(':')
                    dic = {Separate[0]: Separate[1]}
                    for k, v in dic.items():
                        if user1_books == v:
                            print('此书已经被借走!')
                            exit()
                        elif user1_books != v:
                            continue

                else:
                    with open(r'I:\books\books.txt', 'r') as r1stream:
                        r1stream = r1stream.read().splitlines()

                        for book1 in r1stream:
                            if user1_books == book1:

                                with open(r'I:\books\user_book.txt', 'a') as wrstream:
                                    wrstream.write('\n{}\n'.format(user_books))
                                    print('借取成功')
                                    break
                            elif user1_books != book1:
                                continue

                        else:
                            print('借取的书籍不存在！')
                break
    else:
        print('退出图书管理系统')


borrow()


# 用户还书功能
# 用户登陆系统,从user_books表中查找对应的用户及书籍，找到后将其剔除即可！
def still():
    login()
    print('-----------进入书籍退还功能------------')
    username = input("请输入你的姓名：")
    book = input('请输入退还的书籍名：')

    user_books = username + ':' + book

    with open(r'I:\books\user_book.txt', 'r+', encoding='UTF-8') as rstream:
        rstream = rstream.read().splitlines()

        while True:
            for books in rstream:
                if user_books == books:  # True?
                    print('退还成功！')
                    break
                elif user_books != books:  # False?
                    continue
            else:
                print('查找不到该书籍，请检查是否填写错误！')
            break

# still()
