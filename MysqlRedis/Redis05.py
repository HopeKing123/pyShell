# -- coding: utf-8 --
"""学习文档：https://www.jianshu.com/p/2639549bedc8"""
import random

from redis import Redis

conn = Redis(host='xxx.xxx.xxx.xxx', port=6379, db=0, password=None, encoding="utf-8", decode_responses=True)

# 2.redis基本命令 list 列表

# 1.lpush(self, name, *values) - 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
# conn.lpush('list1', 11, 22, 33)
# print(conn.lrange('list1', 0,-1))

# 2.rpush(self, name, *values) - 将“值”放到列表“名称”的末尾``
# 表示从右向左操作
# conn.rpush('list2', 11, 22, 33)
# # 列表长度
# print(conn.llen('list2'))
# # 切片取出值，范围是索引号0-3
# print(conn.lrange('list2', 0, 3))

# 3.lpushx(self, name, *values) - 只有当 key 已经存在并且存着一个 list 的时候，在这个 key 下面的 list 的头部插入 value。 与 LPUSH 相反，当 key
# 不存在的时候不会进行任何操作。
# conn.lpush('list3', 77)
# print(conn.lrange('list03', 0, -1))
# conn.lpushx('list03', 88)
# print(conn.lrange('list03', 0, -1))

# 4.rpushx(self, name, value) - 将值 value 插入到列表 key 的表尾, 当且仅当 key 存在并且是一个列表。 和 RPUSH 命令相反, 当 key 不存在时，RPUSHX 命令什么也不做。
# conn.rpush('list4', 22)
# print(conn.lrange('list4', 0, -1))
# conn.rpushx('list4', 99)
# print(conn.lrange('list4', 0, -1))

# 5.linsert(self, name, where(BEFORE或AFTER), refvalue, value) - 把 value 插入存于 key 的列表中在基准值 pivot 的前面或后面。当 key
# 不存在时，这个list会被看作是空list，任何操作都不会发生。 当 key 存在，但保存的不是一个list的时候，会返回error。
# conn.lpush('list5',11)
# print(conn.lrange('list5', 0, -1))
# conn.linsert('list5', 'before', '11', '80')
# print(conn.lrange('list5', 0, -1))

# 6.lset(self, name, index, value) - 设置 index 位置的list元素的值为 value(修改原有value为现有value)。 当index超出范围时会返回一个error。
# conn.rpush('list6', 'one')
# conn.rpush('list6', 'two')
# conn.rpush('list6', 'three')
# print(conn.lrange('list6', 0, -1))
# conn.lset('list6', 0, 'five')
# conn.lset('list6', 1, 'four')
# print(conn.lrange('list6', 0, -1))

# 7.lrem(self, name, count, value) - 从存于 key 的列表里移除前 count 次出现的值为 value 的元素。
"""
这个 count 参数通过下面几种方式影响这个操作：
count > 0: 从头往尾移除值为 value 的元素。
count < 0: 从尾往头移除值为 value 的元素。
count = 0: 移除所有值为 value 的元素。
比如， LREM list -2 “hello” 会从存于 list 的列表里移除最后两个出现的 “hello”。
需要注意的是，如果list里没有存在key就会被当作空list处理，所以当 key 不存在的时候，这个命令会返回 0。
"""
# conn.rpush('list7', 'hello')
# conn.rpush('list7', 'hello')
# conn.rpush('list7', 'foo')
# conn.rpush('list7', 'kaka')
# conn.rpush('list7', 'hello')
# print(conn.lrange('list7', 0, -1))
# conn.lrem('list7', -2, 'hello')
# print(conn.lrange('list7', 0, -1))

# 8.lpop(self, name, count=None) - 移除并且返回 key 对应的 list 的第一个元素。
# print(conn.lpop('list7'))

# 9.ltrim(self, name, start, end) - 修剪(trim)一个已存在的 list，这样 list 就会只包含指定范围的指定元素。start 和 stop 都是由0开始计数的， 这里的 0
# 是列表里的第一个元素（表头），1 是第二个元素，以此类推。
"""
例如： LTRIM foobar 0 2 将会对存储在 foobar 的列表进行修剪，只保留列表里的前3个元素。
start 和 end 也可以用负数来表示与表尾的偏移量，比如 -1 表示列表里的最后一个元素， -2 表示倒数第二个，等等。
超过范围的下标并不会产生错误：如果 start 超过列表尾部，或者 start > end，结果会是列表变成空表（即该 key 会被移除）。 如果 end 超过列表尾部，Redis 会将其当作列表的最后一个元素。

LTRIM 的一个常见用法是和 LPUSH / RPUSH 一起使用。 例如：

LPUSH mylist someelement
LTRIM mylist 0 99
这一对命令会将一个新的元素 push 进列表里，并保证该列表不会增长到超过100个元素。这个是很有用的，比如当用 Redis 来存储日志。 
需要特别注意的是，当用这种方式来使用 LTRIM 的时候，操作的复杂度是 O(1) ， 因为平均情况下，每次只有一个元素会被移除。
"""
# conn.rpush('list8', 'one')
# conn.rpush('list8', 'two')
# conn.rpush('list8', 'three')
# conn.ltrim('list8', 1, -1)
# print(conn.lrange('list8', 0, -1))

# 10.lindex(self, name, index) - 返回列表里的元素的索引 index 存储在 key 里面。 下标是从0开始索引的，所以 0 是表示第一个元素， 1 表示第二个元素，并以此类推。
"""负数索引用于指定从列表尾部开始索引的元素。在这种方法下，-1 表示最后一个元素，-2 表示倒数第二个元素，并以此往前推。
当 key 位置的值不是一个列表的时候，会返回一个error。"""
# conn.lpush('list9', 'World')
# conn.lpush('list9', 'Hello')
# print(conn.lindex('list9', 0))
# print(conn.lindex('list9', 1))

# 11.rpoplpush(self, src, dst) - 原子性地返回并移除存储在 source 的列表的最后一个元素（列表尾部元素）， 并把该元素放入存储在 destination 的列表的第一个元素位置（列表头部）。
"""
例如：假设 source 存储着列表 a,b,c， destination存储着列表 x,y,z。 执行 RPOPLPUSH 得到的结果是 source 保存着列表 a,b ，而 destination 保存着列表 c,x,y,z。
如果 source 不存在，那么会返回 nil 值，并且不会执行任何操作。 如果 source 和 destination 是同样的，那么这个操作等同于移除列表最后一个元素并且把该元素放在列表头部， 所以这个命令也可以当作是一个旋转列表的命令。
"""
# conn.rpush('list10', 'one')
# conn.rpush('list10', 'two')
# conn.rpush('list10', 'three')
# print(conn.lrange('list10', 0, -1))
# conn.rpoplpush('list10', 'list11')
# print(conn.lrange('list11', 0, -1))

# 12.brpoplpush(self, src, dst, timeout=0) - BRPOPLPUSH 是 RPOPLPUSH 的阻塞版本。
"""
当 source 包含元素的时候，这个命令表现得跟 RPOPLPUSH 一模一样。 当 source 是空的时候，Redis将会阻塞这个连接，直到另一个客户端 push 元素进入或者达到 timeout 时限。 timeout 为 0 能用于无限期阻塞客户端。
"""
# print(conn.lrange('list11', 0, -1))
# conn.brpoplpush('list11', 'list12', timeout=2)
# print(conn.lrange('list12', 0, -1))

# 13.blpop(self, keys, timeout=0) - blpop是lpop的阻塞版本,这是因为当给定列表内没有任何元素可供弹出的时候，连接将被 BLPOP 命令阻塞。当给定多个 key 参数时，按参数 key
# 的先后顺序依次检查各个列表，弹出第一个非空列表的头元素。
"""
非阻塞行为
当 BLPOP 被调用时，如果给定 key 内至少有一个非空列表，那么弹出遇到的第一个非空列表的头元素，并和被弹出元素所属的列表的名字 key 一起，组成结果返回给调用者。
当存在多个给定 key 时， BLPOP 按给定 key 参数排列的先后顺序，依次检查各个列表。 
假设 key list1 不存在，而 list2 和 list3 都是非空列表。考虑以下的命令：
BLPOP list1 list2 list3 0
BLPOP 保证返回一个存在于 list2 里的元素（因为它是从 list1 –> list2 –> list3 这个顺序查起的第一个非空列表）。
当 BLPOP 命令引起客户端阻塞并且设置了一个非零的超时参数 timeout 的时候， 若经过了指定的 timeout 仍没有出现一个针对某一特定 key 的 push 操作，则客户端会解除阻塞状态并且返回一个 nil 的多组合值(multi-bulk value)。
timeout 参数表示的是一个指定阻塞的最大秒数的整型值。当 timeout 为 0 是表示阻塞时间无限制。
"""
# conn.lpush('list13', 1, 2, 3, 4)
# conn.lpush('list14', 5, 6, 7, 8)
# while True:
#     conn.blpop(["list13", "list14"], timeout=1)
#     print(conn.lrange("list13", 0, -1), conn.lrange("list14", 0, -1))


