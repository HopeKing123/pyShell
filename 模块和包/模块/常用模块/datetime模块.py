# time和datetime模块

# time模块
import re
import time

# 时间戳,返回自 Epoch 以来的当前时间（以秒为单位）。
t = time.time()
print(t)

# 延迟执行
# time.sleep(1)

# 将时间戳转成字符串
s = time.ctime(t)
print(s)

# 以元组结构的形式将时间戳转成字符串,可以取相应的值
t1 = time.localtime(t)
print(t1)
print(t1.tm_year)
# 将元组转成时间戳
t2 = time.mktime(t1)
print(t2)

# 将时间戳元组转成字符串
t3 = time.strftime('%Y-%m-%d:%M:%S')
print(t3)

# 将字符串转成元组
t4 = time.strptime('2019/06/20', '%Y/%m/%d')
print(t4)

# datetime模块:python处理日期和时间的标准库
"""
datetime模块：
    time 时间
    date 日期 (data 数据)
    datetime 日期时间
    timedelta 时间差
"""

import datetime

# 获取当前日期和时间
"""
注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
如果仅导入import datetime，则必须引用全名datetime.datetime。
datetime.now()返回当前日期和时间，其类型是datetime。
"""
now = datetime.datetime.now()
print(now)

# 获取指定日期和时间
# 指定某个日期和时间，直接用参数构造一个datetime
dt = datetime.datetime(2021, 12, 9, 16, 10)
print(dt)

# datetime转换为timestamp，timestamp是一个浮点数,没有时区概念
dt = datetime.datetime(2021, 12, 13, 10, 16)  # 用指定日期时间创建datetime
print(dt.timestamp())  # 把datetime转换为timestamp

# timestamp转换为datetime，datetime是有时区的.
t = 1639361760.0
print(datetime.datetime.fromtimestamp(t))

# timestamp转换为UTC标准时区时间
t = 1639361760.0
print(datetime.datetime.fromtimestamp(t))  # 本地时间
print(datetime.datetime.utcfromtimestamp(t))  # utc时间

# str转换为datetime
# 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式，注意转换后的datetime是没有时区信息的.
cday = datetime.datetime.strptime('2021-12-13 10:38:00', '%Y-%m-%d %H:%M:%S')
print(type(cday))

# datetime转换为str
# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
now = datetime.datetime.now()
print(now)
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
now = datetime.datetime.now()
print(now)
now1 = now + datetime.timedelta(hours=2)
print(now1)
now2 = now - datetime.timedelta(hours=2)
print(now2)
now3 = now + datetime.timedelta(days=2, hours=2)
print(now3)

# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
tz_utc_8 = datetime.timezone(datetime.timedelta(hours=8))  # 创建时区UTC+8:00
now = datetime.datetime.now()
# 返回一个新的日期时间，其中包含指定字段的新值。
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
print(dt)

# 时区转换
# utcnow():获取当前时间
# 拿到UTC时间,并强制设置时区为UTC+0:00
utc_dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
print(utc_dt)

# astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
print(bj_dt)

# astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
print(tokyo_dt)
print(type(tokyo_dt))

"""
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
"""


# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：

def to_timestamp(dt_str, tz_str):
    # math尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none.
    ftz = re.match(r'(.{3})(.+)\:(.+)',tz_str)
    # group()在正则表达式中用于获取分段截获的字符串
    ttz = int(ftz.group(2))
    cday = datetime.datetime.strptime(dt_str,"%Y-%m-%d %H:%M:%S")
    # c1 = datetime.datetime.timestamp(cday)
    utc_time = cday.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=ttz)))
    return utc_time.timestamp()


# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')













