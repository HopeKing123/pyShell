# -- coding: utf-8 --
# 导入redis包中的类
from redis import Redis

# 连接redis数据库,配置参数,decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。
conn = Redis(host='xxx.xxx.xxx.xxx', port=6379, db=0, password=None, encoding="utf-8",decode_responses=True)

# 调用set方法，存入键值对。
conn.set('name', 'zhangsan')

# 打印key的value
# print(conn['name'])

# 取出键name对应的值
print(conn.get('name'))

# 打印key的类型
# print(type(conn.get('name')))

# 关闭连接
conn.close()