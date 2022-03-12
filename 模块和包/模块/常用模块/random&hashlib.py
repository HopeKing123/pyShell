# random
import random

# random()方法返回0至1之间的随机数
ran = random.random()
print(ran)

# randrange从指定范围内,按指定基数递增的集合中获取一个随机数，默认步长为1
# 语法：random.randrange(start,stop,step)
ran = random.randrange(1, 10, 2)
print(ran)

# randint用于生成一个指定范围内的整数，其中参数a是下限，参数b是上限
ran = random.randint(1, 10)
print(ran)

# choice从序列中获取一个随即元素，参数sequence表示一个有序类型.
# sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。
list1 = ['zhangsan', 'lisi', 'wangwu', 'maliu']
ran = random.choice(list1)
print(ran)

# shuffle 将一个列表中的元素打乱
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ran = random.shuffle(list2)
print(list2)


# 验证码 大小写字母与数字的组合
# chr函数把数字变成字母,ord函数将字母转陈Unicode码
def func():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0, 9))
        ran2 = chr(random.randint(65, 90))
        ran3 = chr(random.randint(97, 122))

        r = random.choice([ran1, ran2, ran3])
        code += r
    return code


code = func()
print(code)

# hashlib
"""
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
什么是摘要算法呢？摘要算法又称哈希算法、散列算法。
它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
"""
import hashlib

# md5机密，md5无法识别中文必须encode转utf-8
msg = "今天中午吃什么?"
md5 = hashlib.md5(msg.encode('utf-8'))

# 查看加密数据
print(md5.hexdigest())

# sha1
sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest())

# sha256
sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest())

print("##################################################")


# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False:
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }


def login(user, password):
    password = hashlib.md5(password.encode('utf-8'))

    # 判断user是否存在于db中
    if user in db:
        return password.hexdigest() == db[user]  # 取key(user)的值与password进行判断
    return False


# 测试:
# assert：断言函数是对表达式布尔值的判断，要求表达式计算值必须为真,如果表达式为假，触发异常，如果表达式为真，不执行任何操作.
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')


# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
# db = {}
#
#
# def register(username, password):
#     # 将get_md5函数加密的值写入db字典中.
#     db[username] = get_md5(password + username + 'the-Salt')


# 然后，根据修改后的MD5算法实现用户登录的验证：
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        # 将序列中的元素以指定的字符连接生成一个新的字符串
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        # 将用户密码及字符串md5加密
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    if username in db:
        return db[username].password == get_md5(password + db[username].salt)
    return False  # raise ValueError('用户名不存在')


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


# hmac算法
"""
Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1.
"""
# 首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下：
import hmac

message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())


# 练习
def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        # 为username生成key
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        print(self.key)
        self.password = hmac_md5(self.key, password)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    # 可以调用key是因为在db中有User类的引用
    print(db[username].key)
    if username in db:
        return db[username].password == hmac_md5(db[username].key,password)
    return False


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')