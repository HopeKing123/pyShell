# -- coding: utf-8 --
"""
redis-py 使用 connection pool 来管理对一个 redis server 的所有连接，避免每次建立、释放连接的开销。
默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后(redis)作为参数 Redis，这样就可以实现多个 Redis 实例共享一个连接池。
"""
from redis import ConnectionPool,Redis
# 创建Redis连接池
pool = ConnectionPool(host='xxx.xxx.xxx.xxx', port=6379, db=0, password=None, encoding="utf-8",decode_responses=True)

# 连接Pool池,Redis类操作redis数据库
conn = Redis(connection_pool=pool)

# 设置键值对
conn.set('name01','lisi')

# 取出键值对
print(conn.get('name01'))
