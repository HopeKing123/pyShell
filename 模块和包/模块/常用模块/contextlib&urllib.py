# contextlib:对文件上下文进行管理
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的.
class Query:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("Begin")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('Bob') as q:
    q.query()

# @contextmanager
# 编写__enter__和__exit__仍然很繁琐,因此Python的标准库contextlib提供了更简单的写法
from contextlib import contextmanager


class Query:

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
with create_query('Bob') as q:
    q.query()


# 在某段代码执行前后自动执行特定代码.
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

"""
代码的执行顺序是：

with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。
因此，@contextmanager让我们通过编写generator来简化上下文管理。
"""

# @closing: 经过@contextmanager装饰的generator
# 如果一个对象没有实现上下文,就不能把它用于with语句.这个时候,可以用closing()来把该对象变为上下文对象,例如:用with语句使用urlopen():
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()


# 它的作用就是把任意对象变为上下文对象，并支持with语句。
print('-------------------------------------------------------------------------------------------------------')

# urllib:提供了一系列用于操作URL的功能

# Get
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
from urllib import request

with request.urlopen('https://www.baidu.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

print('#############################################')

# 模拟浏览器发生GET请求,就需要使用Request对象，往Request对象添加HTTP头，就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
req = request.Request('http://douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))


# POST
# 如果要以POST发生一个请求，只需要把参数data以bytes形式传入.
# 模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email:')
passwd = input('Password:')
login_data = parse.urlencode([
    ('username',email),
    ('password',passwd),
    ('entry','mweibo'),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# 登录成功返回200



