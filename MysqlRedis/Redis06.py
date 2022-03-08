# -- coding: utf-8 --
import random

from redis import Redis

conn = Redis(host='xxx.xxx.xxx.xxx', port=6379, db=0, password=None, encoding="utf-8", decode_responses=True)

# 2.redis基本命令 set 集合

# 1.sadd(self, name, *values) - 添加一个或多个指定的member元素到集合的 key中.指定的一个或者多个元素member 如果已经在集合key中存在则忽略.如果集合key 不存在，则新建集合key,
# 并添加member元素到集合key中.
# conn.sadd('set1', 'Hello', 'World', 'Marich')
# 集合的长度
# print(conn.scard('set1'))
# 获取集合中所有的成员
# print(conn.smembers('set1'))

# 2.scard(self, name) - 返回集合存储的key的基数 (集合元素的数量).
# print(conn.scard('set1'))

# 3.smembers(self, name) - 返回key集合所有的元素. 可能会出现阻塞服务器的问题
# print(conn.smembers('set1'))

# sscan - 用于迭代SET集合中的元素。
"""
注意的是SSCAN, HSCAN ,ZSCAN命令的第一个参数总是一个key； SCAN 命令则不需要在第一个参数提供任何key，因为它迭代的是当前数据库中的所有key。

SCAN命令是一个基于游标的迭代器。这意味着命令每次被调用都需要使用上一次这个调用返回的游标作为该次调用的游标参数，以此来延续之前的迭代过程
当SCAN命令的游标参数被设置为 0 时， 服务器将开始一次新的迭代， 而当服务器向用户返回值为 0 的游标时， 表示迭代已结束。
注意的是SSCAN, HSCAN ,ZSCAN命令的第一个参数总是一个key； SCAN 命令则不需要在第一个参数提供任何key，因为它迭代的是当前数据库中的所有key。
"""
# print(conn.sscan('set1'))

# sscan_iter(name, match=None, count=None) - 获取集合中所有的成员--迭代器的方式
# conn.sadd('set1', 'Hello', 'World', 'Marich')
# for i in conn.sscan_iter('set1'):
#     print(i)

# 4.sdiff(self, keys, *args) - 返回一个集合与给定集合的差集的元素.
# conn.sadd('set1', 'Hello', 'World', 'Marich')
# conn.sadd('set2', 'Hello', 'World', 'kaka')
# 获取集合中所有的成员
# print(conn.smembers('set1'))
# 获取集合中所有的成员
# print(conn.smembers('set2'))
# 在集合set1但是不在集合set2中
# print(conn.sdiff('set1', 'set2'))
# 在集合set2但是不在集合set1中
# print(conn.sdiff('set2', 'set1'))

# 5.sdiffstore(self, dest, keys, *args) - 该命令类似于 SDIFF, 不同之处在于该命令不返回结果集，而是将结果存放在destination集合中.如果destination已经存在,
# 则将其覆盖重写.
# conn.sadd('set1', 'Hello', 'World', 'Marich')
# conn.sadd('set2', 'Hello', 'World', 'kaka')
# conn.sdiffstore('set3', 'set1', 'set2')
# print(conn.smembers('set3'))

# 6.sinter(self, keys, *args) - 返回指定所有的集合的成员的交集.
# print(conn.sinter('set1', 'set2'))

# 7.sinterstore(self, dest, keys, *args) - 这个命令与SINTER命令类似, 但是它并不是直接返回结果集,而是将结果保存在 destination集合中.
# 如果destination 集合存在, 则会被重写.
# conn.sinterstore('set4', 'set1', 'set2')
# print(conn.smembers('set4'))

# sunion - 获取多个name对应的集合的并集
# print(conn.sunion('set1', 'set2'))

# sunionstore -
# conn.sunionstore('set5', 'set1', 'set2')
# print(conn.smembers('set5'))

# 8.sismember(self, name, value) - 返回成员 member 是否是存储的集合 key的成员.
# conn.sadd('set1', 'Hello', 'World', 'Marich')
# print(conn.sismember('set1', 'Hello'))
# print(conn.sismember('set1', 'lisi'))

# 9.smove(self, src, dst, value) - 将member从source集合移动到destination集合中. 对于其他的客户端,在特定的时间元素将会作为source或者destination集合的成员出现.
"""
如果source 集合不存在或者不包含指定的元素,这smove命令不执行任何操作并且返回0.
否则对象将会从source集合中移除，并添加到destination集合中去，如果destination集合已经存在该元素，则smove命令仅将该元素充source集合中移除. 如果source 和destination不是集合类型,则返回错误.
"""
# conn.sadd('set1', 'Hello', 'World', 'Marich')
# conn.sadd('set2', 'Hello', 'World', 'kaka')
# conn.smove('set1', 'set6', 'Marich')
# print(conn.smembers('set6'))

# 10.spop(self, name, count=None) - 从集合移除一个成员，并将其返回,说明一下，集合是无序的，所有是随机删除的
# conn.sadd('set1', 'Hello', 'World', 'Marich')
# conn.spop('set1')
# print(conn.smembers('set1'))

# 11.srem(self, name, *values) - 在集合中移除指定的key元素. 如果指定的元素不是key集合中的元素则忽略 如果key集合不存在则被视为一个空的集合，该命令返回0.
# 如果key的类型不是一个集合,则返回错误.
# conn.srem('set1', 'Hello')
# print(conn.smembers('set1'))
