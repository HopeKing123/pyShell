# -- coding: utf-8 --

# 2.redis基本命令 有序set
# 有序集合按照分数以递增的方式进行排序。相同的成员（member）只存在一次，有序集合不允许存在重复的成员。
import time

from redis import Redis

conn = Redis(host='XXX.XXX.XXX.XXX', port=6379, db=0, password=None, encoding="utf-8", decode_responses=True)

# 1.zadd - 将所有指定的成员添加到键为key的有序集合（sorted set）里面。
"""
添加时可以指定多个分数/成员（score/member）对。 
如果指定添加的成员已经是有序集合里面的成员，则会更新改成员的分数（scrore）并更新到正确的排序位置。
如果key不存在，将会创建一个新的有序集合（sorted set）并将分数/成员（score/member）对添加到有序集合，就像原来存在一个空的有序集合一样。
如果key存在，但是类型不是有序集合，将会返回一个错误应答。

ZADD参数：
ZADD命令在key后面分数/成员对前面支持一些参数.
    XX：仅仅更新存在的成员，不添加新成员
    NX：不更新存在的成员。只添加新成员。
    CH(changed)：将返回值修改为更改的元素数。更改的元素包括添加的新元素和分数更改的元素。
    INCR：对成员的分数进行递增操作。
    LT：仅当新分数小于当前分数时才更新现有元素。此标志不阻止添加新元素。
    GT：仅当新分数大于当前分数时才更新现有元素。此标志不阻止添加新元素。
ZADD的返回值根据指定的模式而变化。在没有选项的情况下，ZADD返回添加到排序集的新元素数。
``NX``、`LT``和`GT``是相互排斥的选项。
如果用户将所有元素设置相同分数（例如0），有序集合里面的所有元素将按照字典顺序进行排序，范围查询元素可以使用ZRANGEBYLEX命令。
"""
# 添加
# conn.zadd("zset1", mapping={"one": 1, "two": 2})
# 集合长度
# print(conn.zcard('zset1'))
# 获取有序集合中所有元素
# print(conn.zrange('zset1', 0, -1))
# 获取有序集合中所有元素和分数
# print(conn.zrange('zset1', 0, -1, withscores=True))

# 2.zcard - 返回key的有序集元素个数。
# 集合长度
# print(conn.zcard('zset1'))

# 3.zrange - 返回存储在有序集合key中的指定范围的元素。
"""
当你需要元素从最高分到最低分排列时，请参阅ZREVRANGE（相同的得分将使用字典倒序排序）。
参数start和stop都是基于零的索引，即0是第一个元素，1是第二个元素，以此类推。 它们也可以是负数，表示从有序集合的末尾的偏移量，其中-1是有序集合的最后一个元素，-2是倒数第二个元素，等等。
start和stop都是全包含的区间，因此例如ZRANGE myzset 0 1将会返回有序集合的第一个和第二个元素。
超出范围的索引不会产生错误。 如果start参数的值大于有序集合中的最大索引，或者start > stop，将会返回一个空列表。 如果stop的值大于有序集合的末尾，Redis会将其视为有序集合的最后一个元素。
可以传递WITHSCORES选项，以便将元素的分数与元素一起返回。这样，返回的列表将包含value1,score1,...,valueN,scoreN，而不是value1,...,valueN。 客户端类库可以自由地返回更合适的数据类型（建议：具有值和得分的数组或记录）。
"""
# 获取有序集合中所有元素
# print(conn.zrange('zset1', 0, -1,withscores=True))

# 4.zrevrange - 返回有序集key中，指定区间内的成员。其中成员的位置按score值递减(从大到小)来排列。具有相同score值的成员按字典序的反序排列。
# 添加
# conn.zadd("zset2", mapping={"one": 1, "two": 2, "three": 3})
# print(conn.zrevrange("zset2", 0, -1, withscores=True))

# 5.zrangebyscore - 返回key的有序集合中的分数在min和max之间的所有元素（包括分数等于max或者min的元素）。元素被认为是从低分到高分排序的。
"""
从排序集“name”返回一系列值，分数介于“min”和“max”之间。
如果指定了``start``和``num`'，则返回范围的一部分。
`withscores`表示返回分数和值。返回类型是（值、分数）对的列表
`score_cast_func``用于转换分数返回值的可调用函数
"""
# for i in range(1, 30):
#     element = "n" + str(i)
#     conn.zadd("zset3", mapping={element: i})
# 在分数是15-25之间，取出符合条件的元素k
# print(conn.zrangebyscore("zset3", 15, 25))
# 在分数是12-22之间，取出符合条件的元素（带分数）
# print(conn.zrangebyscore("zset3", 12, 22, withscores=True))

# 6.zrevrangebyscore - 返回有序集合中指定分数区间内的成员，分数由高到低排序。
"""
语法：
    ZREVRANGEBYSCORE key max min WITHSCORES LIMIT offset count
说明：

指令	                是否必须	        说明
ZREVRANGEBYSCORE	    是	        指令
key	                    是	        有序集合键名称
max	                    是	        最大分数值,可使用"+inf"代替
min	                    是	        最小分数值,可使用"-inf"代替
WITHSCORES	            否	        将成员分数一并返回
LIMIT	                否	        返回结果是否分页,指令中包含LIMIT后offset、count必须输入
offset	                否	        返回结果起始位置
count	                否	        返回结果数量

提示：
"max" 和 "min"参数前可以加 "(" 符号作为开头表示小于, "(" 符号与成员之间不能有空格
可以使用 "+inf" 和 "-inf" 表示得分最大值和最小值
max" 和 "min" 不能反, "max" 放后面 "min"放前面会导致返回结果为空
计算成员之间的成员数量不加 "(" 符号时,参数 "min" 和 "max" 的位置也计算在内。
ZREVRANGEBYSCORE集合中按得分从高到底排序,所以"max"在前面,"min"在后面, ZRANGEBYSCORE集合中按得分从底到高排序,所以"min"在前面,"max"在后面。
"""
# 按分数倒序返回成员
""""+inf" 或者 "-inf" 来表示记录中最大值和最小值。 "(" 左括号来表示小于某个值。目前只支持小于操作的 "(" 左括号, 右括号(大于)目前还不能支持。"""
# conn.zadd("myzset1", mapping={"one": 1, "two": 2, "three": 3})
# print(conn.zrevrangebyscore("myzset1", "+inf", "-inf", withscores=True))
# print(conn.zrevrangebyscore("myzset1", 2, 1, withscores=True))
# print(conn.zrevrangebyscore("myzset1", 2, "(1", withscores=True))

# 分页返回数据
"""
可以通过 LIMIT 对满足条件的成员列表进行分页。
一般会配合 "+inf" 或者 "-inf" 来表示最大值和最小值。
# LIMIT输出下标为0，1元素
redis> ZREVRANGEBYSCORE myzset +inf (2 WITHSCORES LIMIT 0 1 
1) "three"
2) "3"
# LIMIT输出下标为2，3元素
redis> ZREVRANGEBYSCORE myzset +inf (2 WITHSCORES LIMIT 2 3
(empty list or set)
"""

# 7.zscan - 用于迭代SortSet集合中的元素和元素对应的分值(默认按照分数顺序排序)
"""
基本用法：
注意SSCAN, HSCAN ,ZSCAN命令的第一个参数总是一个key； 
SCAN命令是一个基于游标的迭代器。这意味着命令每次被调用都需要使用上一次这个调用返回的游标作为该次调用的游标参数，以此来延续之前的迭代过程
当SCAN命令的游标参数被设置为 0 时， 服务器将开始一次新的迭代， 而当服务器向用户返回值为 0 的游标时， 表示迭代已结束。
"""
# print(conn.zscan('zset3'))

# 8.zscan_iter - 于迭代SortSet集合中的元素和元素对应的分值(迭代器)
# 使用ZSCAN命令生成一个迭代器，这样客户端就不需要记住光标的位置。
"""
``match``允许按模式筛选键
``count``允许提示返回的最小数量
``score_cast_func``用于转换分数返回值的可调用函数
"""
# for i in conn.zscan_iter('zset3'):
# print(i)

# 9.zcount - 返回有序集key中，score值在min和max之间(默认包括score值等于min或max)的成员。
# conn.zadd("zset4", mapping={"one": 1, "two": 2, "three": 3})
# print(conn.zcount("zset4", "-inf", "+inf"))
# print(conn.zcount("zset4", 1, 2))

# 10.zincrby - 自增name对应的有序集合的 name 对应的分数
# conn.zadd("zset5", mapping={"one": 1, "two": 2, "three": 3})
# # print(conn.zrange('zset5', 0, -1, withscores=True))
# conn.zincrby('zset5', amount=2, value="one")
# print(conn.zrange('zset5', 0, -1, withscores=True))

# 11.zrank - 返回有序集key中成员的排名。
"""
其中有序集成员按score值递增(从小到大)顺序排列。排名以0为底，也就是说，score值最小的成员排名为0。
使用ZREVRANK命令可以获得成员按score值递减(从大到小)排列的排名。
"""
# 这里按照分数顺序（从小到大）
# print(conn.zrank('zset3', 'n1'))
# print(conn.zrank('zset3', 'n6'))

# 12.zrevrank - 从大到小排序
# 这里按照分数倒序（从大到小）
# print(conn.zrevrank('zset3','n1'))

# 13.zrem - 指定值删除
# print(conn.zrange("zset4", 0, -1, withscores=True))
# conn.zrem('zset4', 'one')
# print(conn.zrange("zset4", 0, -1, withscores=True))

# 14.zremrangebyrank - 移除有序集key中，指定排名(rank)区间内的所有成员。
"""
下标参数start和stop都以0为底，0处是分数最小的那个元素。这些索引也可是负数，表示位移从最高分处开始数。例如，-1是分数最高的元素，-2是分数第二高的，依次类推。
"""
# for i in range(1, 30):
#     element = "n" + str(i)
#     conn.zadd("zset7", mapping={element: i})
# 删除有序集合中的索引号是11, 22的元素
# conn.zremrangebyrank("zset7", 11, 22)
# print(conn.zrange('zset7', 0, -1,withscores=True))

# 16.zremrangebyscore - 移除有序集key中，所有分数值介于min和max之间(包括等于min或max)的成员。
# conn.zadd('zset8', mapping={"one": 1, "two": 2, "three": 3})
# conn.zremrangebyscore('zset8', "-inf", "(2")
# print(conn.zrange("zset8", 0, -1,withscores=True))

# 17.zscore - 返回有序集key中，成员member的分数值。
"""如果member元素不是有序集key的成员，或key不存在，返回nil。"""
# conn.zadd('zset9', mapping={"one": 1})
# print(conn.zscore("zset9", "one"))

"""其他常用命令"""
# 1.delete - 删除由名称指定的一个或多个键
# conn.set('name','zhangsan')
# print(conn.get('name'))
# conn.delete('name')
# print(conn.get('name'))

# 2.exists - 返回key是否存在。
"""
返回值：1 如果key存在 0如果key不存在
"""
# conn.set('key1', 'Hello')
# print(conn.exists('key1'))

# 3. keys - 查找所有符合给定模式（条件）pattern（正则表达式）的 key. 可能会出现阻塞服务器的问题
"""
KEYS * 匹配数据库中所有 key 。
KEYS h?llo 匹配 hello ， hallo 和 hxllo 等。
KEYS hllo 匹配 hllo 和 heeeeello 等。
KEYS h[ae]llo 匹配 hello 和 hallo ，但不匹配 hillo
"""
# conn.mset(mapping={'k1': 'v1', 'k2': 'v2', 'k3': 'v3'})
# print(conn.keys('k?'))
# print(conn.keys("*"))

# 4.expire - 设置key的过期时间，超过时间后，将会自动删除该key。
"""
超时后只有对key执行DEL命令或者SET命令或者GETSET时才会清除。这意味着，从概念上讲所有改变key的值的操作都会使他清除。
例如，INCR递增key的值，执行LPUSH操作，或者用HSET改变hash的field所有这些操作都会触发删除动作。
使用PERSIST命令可以清除超时，使其变成一个永久的key。
如果key被RENAME命令修改，相关的超时时间会转移到新key上面。
如果key被RENAME命令修改，比如原来就存在Key_A,然后调用RENAME Key_B Key_A命令，这时不管原来Key_A是永久的还是设置为超时的，都会由Key_B的有效期状态覆盖。
刷新过期时间
对已经有过期时间的key执行EXPIRE操作，将会更新它的过期时间。有很多应用有这种业务场景，例如记录会话的session。
"""
# conn.lpush("list01", 11, 12)
# conn.expire("list01", time=3)
# print(conn.lrange('list01', 0, -1))
# time.sleep(3)
# print(conn.lrange('list01', 0, -1))

# 5.rename - 将key重命名为newkey，如果key与newkey相同，将返回一个错误。如果newkey已经存在，则值将被覆盖。
# conn.lpush("list02", 9, 88)
# print(conn.lrange("list02", 0, -1))
# conn.rename("list02", "list03")
# print(conn.lrange("list03", 0, -1))

# 6.randomkey - 从当前数据库返回一个随机的key
# print(conn.randomkey())

# 7.type - 获取name对应值的类型
# print(conn.type('list03'))

# 8.scan - 用于迭代当前数据库中的key集合。
"""
注意：SMEMBERS 命令可以返回集合键当前包含的所有元素，但是对于SCAN这类增量式迭代命令来说，有可能在增量迭代过程中，集合元素被修改，对返回值无法提供完全准确的保证。
SCAN命令是一个基于游标的迭代器。这意味着命令每次被调用都需要使用上一次这个调用返回的游标作为该次调用的游标参数，以此来延续之前的迭代过程
当SCAN命令的游标参数被设置为 0 时， 服务器将开始一次新的迭代， 而当服务器向用户返回值为 0 的游标时， 表示迭代已结束。
"""
# print(conn.scan(0))

# 9.scan_iter - 使用SCAN命令生成一个迭代器，这样客户端就不需要记住光标的位置。
"""
``match``允许按模式筛选键
``count``为Redis提供了一个关于每批返回的密钥数的提示。
``_type``按特定的Redis类型过滤返回的值。Stock Redis实例允许以下类型：散列、列表、集合、流、字符串、ZSET。此外，Redis模块还可以公开其他类型。
"""
# conn.sadd("set1", "Hello", "world", "Wang")
# for i in conn.sscan_iter("set1"):
#     print(i)

# 10.get - 返回key的value。
"""
如果key不存在，返回特殊值nil。如果key的value不是string，就返回错误，因为GET只处理string类型的values。
"""
# conn.set('name','lisi')
# print(conn.get('name'))

# 11.dbsize - 返回当前数据里面keys的数量。
# print(conn.dbsize())

# 12.save -  执行"检查点"操作，将数据写回磁盘。保存时阻塞
# conn.save()

# 13.flushdb - 清空数据库中的所有数据
# conn.flushdb()
