# -- coding: utf-8 --
import random

from redis import Redis

conn = Redis(host='xxx.xxx.xxx.xxx', port=6379, db=0, password=None, encoding="utf-8", decode_responses=True)

# 2.redis基本命令 hash 哈希

# 1.hset - 设置 key 指定的哈希集中指定字段的值。
# 如果 key 指定的哈希集不存在，会创建一个新的哈希集并与 key 关联。
# 如果字段在哈希集中存在，它将被重写。
"""
# 参数(self, name, key=None, value=None, mapping=None)
name对应的hash中设置一个键值对（不存在，则创建；否则，修改）
参数：
name - redis的name（指定hash集key）
key - name对应的hash中的key（指定hash集）
value - name对应的hash中的value（指定hash集value）
"""
# conn.hset('myhash', 'field1', 'Hello')
# print(conn.hget('myhash', 'field1'))

# 2.hmset - 设置 key 指定的哈希集中指定字段的值。该命令将重写所有在哈希集中存在的字段。如果 key 指定的哈希集不存在，会创建一个新的哈希集并与 key 关联（hmset被弃用，现使用hset）
# conn.hset('myhash01', mapping={'k1': 'v1', 'k2': 'v2'})
# # 单个取出
# print(conn.hget('myhash01','k1'))
# # 批量取出
# print(conn.hmget('myhash01','k1','k2'))

# 3.hgetall - 取出所有的键值对
# print(conn.hgetall('myhash'))

# 4.hlen - 返回 key 指定的哈希集包含的字段的数量。
"""
hlen(name)
获取name对应的hash中键值对的个数
"""
# conn.hset('myhash', mapping={'k1': 'k1', 'k2': 'v2'})
# print(conn.hlen('myhash'))

# 5.hkeys(name) - 返回 key 指定的哈希集中所有字段的名字。
# print(conn.hkeys('myhash'))

# 6.hvals(name) - 返回 key 指定的哈希集中所有字段的值。
# print(conn.hvals('myhash'))

# 7.hexists(name, key) - 返回hash里面field是否存在
# print(conn.hgetall('myhash'))
# print(conn.hexists('myhash','k1'))
# print(conn.hexists('myhash','k2'))
# print(conn.hexists('myhash','k3'))

# 8.hdel(name,*keys) - 从 key 指定的哈希集中移除指定的域。在哈希集中不存在的域将被忽略。如果 key 指定的哈希集不存在，它将被认为是一个空的哈希集，该命令将返回0。
# print(conn.hgetall('myhash'))
# conn.hdel('myhash','k2')
# print(conn.hgetall('myhash'))

# 9.hincrby(name, key, amount=1) - 增加 key 指定的哈希集中指定字段的数值。如果 key 不存在，会创建一个新的哈希集并与 key 关联。
# 如果字段不存在，则字段的值在该操作执行前被设置为 0 HINCRBY 支持的值的范围限定在 64位 有符号整数
# conn.hset('myhash', 'k2', random.randint(1, 10))
# print(conn.hget('myhash', 'k2'))
# conn.hincrby('myhash', 'k2', amount=1)
# print(conn.hget('myhash', 'k2'))

# 10.hincrbyfloat(self, name, key, amount=1.0) - 为指定key的hash的field字段值执行float类型的increment加。
"""
如果field不存在，则在执行该操作前设置为0.如果出现下列情况之一，则返回错误：
field的值包含的类型错误(不是字符串)。
当前field或者increment不能解析为一个float类型。
"""
# conn.hset('myhash', 'k3', 10.50)
# print(conn.hget('myhash', 'k3'))
# conn.hincrbyfloat('myhash', 'k3', amount=1.0)
# print(conn.hget('myhash', 'k3'))

# 11.hscan(self, name, cursor=0, match=None, count=None) - 增量迭代一个集合元素。
"""
增量式迭代获取，对于数据大的数据非常有用，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而放置内存被撑爆
参数：
name - redis的name
cursor - 游标（基于游标分批取获取数据）
match - 匹配指定key，默认None 表示所有的key
count - 每次分片最少获取个数，默认None表示采用Redis的默认分片个数
第一次：cursor1, data1 = r.hscan('xx', cursor=0, match=None, count=None)
第二次：cursor2, data1 = r.hscan('xx', cursor=cursor1, match=None, count=None)
"""

# 12.hscan_iter(self, name, match=None, count=None) - 利用yield封装hscan创建生成器，实现分批去redis中获取数据
"""
参数：
match，匹配指定key，默认None 表示所有的key
count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数
"""
# for item in conn.hscan_iter('myhash'):
#     print(item)
# # 生成器内存地址
# print(conn.hscan_iter('myhash'))
















