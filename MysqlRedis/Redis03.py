# -- coding: utf-8 --
import random

from redis import Redis

# redis基本命令
conn = Redis(host='XXX.XXX.XXX.XXX', port=6379, db=0, password=None, encoding="utf-8", decode_responses=True)

# redis基本命令
# 1.redis基本命令 String 字符串
"""
set(name, value, ex=None, px=None, nx=False, xx=False)
在 Redis 中设置值，默认，不存在则创建，存在则修改。
参数：
ex - 过期时间（秒）
px - 过期时间（毫秒）
nx - 如果设置为True，则只有name不存在时，当前set操作才执行
xx - 如果设置为True，则只有name存在时，当前set操作才执行
"""

# 1.ex - 过期时间（秒） 这里过期时间是3秒，3秒后p，键的值就变成None
# conn.set('name', 'wangwu', ex=3)

# 取出键值对
# print(conn.get('name'))

# 2.px - 过期时间（秒） 这里过期时间是3豪秒，3毫秒后，键的值就变成None
# conn.set('name', 'libai', px=3)

# 取出键值对
# print(conn.get('name'))

# 3.nx - 如果设置为True，则仅当键``number``处的值不存在时，才将其设置为``value`
# 如果键number不存在，那么输出True；如果键number存在，输出None
# print(conn.set('number', random.randint(1, 10), nx=True))

# 4.xx - 如果设置为True，则仅当键``number01``处的值已经存在时，才将其设置为``value`。
# 如果number01已经存在，那么输出True；如果键number01不存在，则输出None
# print(conn.set('number01', random.randint(1, 10), xx=True))

# 5.exat - 在键``number02``上设置以unix时间指定的``ex``秒的过期标志。
# conn.set('number02', random.randint(1, 10), ex=1644817350)
# print(conn.get('number02'))

# 6.pxat - 在键``number03``上设置以unix时间指定的``ex``毫秒的过期标志。
# conn.set('number03', random.randint(1, 10), px=1644817350)
# print(conn.get('number03'))

# 7.keepttl - 如果为True，请保留与密钥关联的生存时间。（从Redis 6.0开始提供）

# 8.get - 如果为True，则将键``name`处的值设置为``value``并返回存储在键处的旧值，如果键不存在，则返回None。（从Redis 6.2开始提供）

# 9.setnx - 将key设置值为value，如果key不存在，这种情况下等同SET命令。 当key存在时，什么也不做。
# conn.setnx('number04', random.randint(1, 10))
# print(conn.get('number04'))

# 10.setex - 设置key对应字符串value，并且设置key在给定的seconds时间之后超时过期。
# conn.setex('number05', 5, random.randint(1, 10))
# 5秒后，取值就变成None
# print(conn.get('number05'))

# 11.psetex - PSETEX和SETEX一样，唯一的区别是到期时间以毫秒为单位,而不是秒。
# conn.psetex('number06', 30, random.randint(1, 10))
# 5秒后，取值就变成None
# print(conn.get('number06'))

# 12.mset - 对应给定的keys(键)到他们相应的values(值)上。
"""
MSET会用新的value替换已经存在的value，就像普通的SET命令一样。
MSET是原子的，所以所有给定的keys是一次性set的。客户端不可能看到这种一部分keys被更新而另外的没有改变的情况。
"""
# conn.mset(mapping={'k1': 'v1', 'k2': 'v2', 'k3': 'v3'})
# print(conn.mget('k1', 'k2', 'k3'))

# mget - 返回所有指定的key的value。对于每个不对应string或者不存在的key，都返回特殊值nil。正因为此，这个操作从来不会失败。
# print(conn.mget('k1', 'k2', 'k3'))

# 13.getset - 自动将key对应到value并且返回原来key对应的value。如果key存在但是对应的value不是字符串，就返回错误。
# # 设置的新值 设置前的值是5
# print(conn.getset('number04', random.randint(1, 10)))

# 14.getrange - 返回key对应的字符串value的子串，这个子串是由start和end位移决定的（两者都在string内）。
# 可以用负的位移来表示从string尾部开始数的下标。所以-1就是最后一个字符，-2就是倒数第二个，以此类推。
# conn.set('abstract', 'This is a magical story')
# 参数(key, start, end)
# print(conn.getrange('abstract', 0, 3))
# print(conn.getrange('abstract', 5, 9))
# print(conn.getrange('abstract', 10, 17))
# print(conn.getrange('abstract', 18, 23))

# 15.setrange - 覆盖key指定的string的一部分，从指定的offset处开始，覆盖value的长度。如果offset比当前key对应string还要长，那这个string后面就补0以达到offset。
# 不存在的keys被认为是空字符串，所以这个命令可以确保key有一个足够大的字符串，能在offset处设置value。
# conn.set('number04', random.randint(1, 10), ex=1700000000)
# 原始值
# print(conn.get('number04'))
# 替换覆盖后的值
# conn.setrange('number04', 0, 9)
# 打印现有值
# print(conn.get('number04'))

# 16.setbit - 设置或者清空key的value(字符串)在offset处的bit值。
# 如果在Redis中有一个对应： n1 = "foo"，那么字符串foo的二进制表示为：01100110 01101111 01101111
# 所以，如果执行 setbit('n1', 7, 1)，则就会将第7位设置为1，那么最终二进制则变成 01100111 01101111 01101111，即："goo"

# 17.getbit - 返回key对应的string在offset处的bit值 当offset超出了字符串长度的时候，这个字符串就被假定为由0比特填充的连续空间。
# print(conn.getbit('number04', 2))

# 18.bitcount - 统计字符串被设置为1的bit数.一般情况下，给定的整个字符串都会被进行计数，通过指定额外的 start 或 end 参数，可以让计数只在特定的位上进行。
# print(conn.bitcount('number04', 0, 11))

# 19.bitop - 对一个或多个保存二进制位的字符串 key 进行位元操作，并将结果保存到 destkey 上。
"""
BITOP 命令支持 AND 、 OR 、 NOT 、 XOR 这四种操作中的任意一种参数：
BITOP AND destkey srckey1 srckey2 srckey3 ... srckeyN ，对一个或多个 key 求逻辑并，并将结果保存到 destkey 。
BITOP OR destkey srckey1 srckey2 srckey3 ... srckeyN，对一个或多个 key 求逻辑或，并将结果保存到 destkey 。
BITOP XOR destkey srckey1 srckey2 srckey3 ... srckeyN，对一个或多个 key 求逻辑异或，并将结果保存到 destkey 。
BITOP NOT destkey srckey，对给定 key 求逻辑非，并将结果保存到 destkey 。
除了 NOT 操作之外，其他操作都可以接受一个或多个 key 作为输入。
执行结果将始终保持到destkey里面。
"""
# 获取Redis中foo1,foo2对应的值，然后将所有的值做位运算（求并集），然后将结果保存 foo3 对应的值中
# conn.set('foo1', 1)
# conn.set('foo2', 2)
# print(conn.mget('foo1', 'foo2'))
# print(conn.bitop("AND", 'foo3', 'foo1', 'foo2'))
# print(conn.mget("foo1", "foo2", "foo3"))

# 20.strlen - 返回key的string类型value的长度。如果key对应的非string类型，就返回错误。
# conn.set('name', 'zhangsan')
# print(conn.strlen('name'))

# 21.incr
"""
对存储在指定key的数值执行原子的加1操作。
如果指定的key不存在，那么在执行incr操作之前，会先将它的值设定为0。
如果指定的key中存储的值不是字符串类型（fix：）或者存储的字符串类型不能表示为一个整数，
那么执行这个命令时服务器会返回一个错误(eq:(error) ERR value is not an integer or out of range)。
这个操作仅限于64位的有符号整型数据。
注意: 由于redis并没有一个明确的类型来表示整型数据，所以这个操作是一个字符串操作。
执行这个操作的时候，key对应存储的字符串被解析为10进制的64位有符号整型数据。
事实上，Redis 内部采用整数形式（Integer representation）来存储对应的整数值，所以对该类字符串值实际上是用整数保存，也就不存在存储整数的字符串表示（String representation）所带来的额外消耗。
"""
# conn.set('foo1', 1)
# conn.set('foo2', 2)
# print(conn.mget('foo1','foo2'))
# conn.incr('foo1',amount=1)
# conn.incr('foo2',amount=1)
# print(conn.mget('foo1','foo2'))

# 22.incrbyfloat - 通过指定浮点数key来增长浮点数(存放于string中)的值. 当键不存在时,先将其值设为0再操作.下面任一情况都会返回错误:
# key 包含非法值(不是一个string).
# 当前的key或者相加后的值不能解析为一个双精度的浮点值.(超出精度范围了)
# conn.set("foo1", "123.0")
# conn.set("foo2", "221.0")
# print(conn.mget("foo1", "foo2"))
# conn.incrbyfloat("foo1", amount=2.0)
# conn.incrbyfloat("foo2", amount=3.0)
# print(conn.mget("foo1", "foo2"))

# 23.decr - 对key对应的数字做减1操作。如果key不存在，那么在操作之前，这个key对应的值会被置为0。
# 如果key有一个错误类型的value或者是一个不能表示成数字的字符串，就返回错误。这个操作最大支持在64位有符号的整型数字。
# conn.decr("number04",amount=2)
# print(conn.get('number04'))

# 24.append - 如果 key 已经存在，并且值为字符串，那么这个命令会把 value 追加到原来值（value）的结尾。
# 如果 key 不存在，那么它将首先创建一个空字符串的key，再执行追加操作，这种情况 APPEND 将类似于 SET 操作。
# conn.append('number04', 11)
# print(conn.get('number04'))

