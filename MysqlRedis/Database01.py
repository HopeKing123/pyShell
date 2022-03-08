# -- coding: utf-8 --
# mysql数据库操作
import mysql.connector

# 创建数据库连接
# 参数(['user', 'password', 'host', 'port', 'unix_socket','database', 'pool_name', 'pool_size'])
conn = mysql.connector.connect(user='root', password='123456', host='xxx.xxx.xxx.xxx', port=3306, database='test')

# 创建游标（实例化操作），检查连接可用性，不可用抛InterfaceError异常
# 参数(self, buffered=None, raw=None, prepared=None, cursor_class=None)
cursor = conn.cursor()

# 创建user表
# execute使用mysql协议执行给定的命令，使用给定的参数执行给定的命令。
# cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user(id, name) values (%s, %s)', ['1', 'Michael'])

# 返回产生或影响的行数
# 返回结果集中的行数
# c = cursor.rowcount
# print(c)

# 提交当前事务
# 执行INSERT等操作后要调用commit()提交事务;
conn.commit()
# 游标关闭
cursor.close()

# 查询：
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

# 关闭
cursor.close()
conn.close