# coding=utf-8
# collections是Python内建的一个集合模块，提供了许多有用的集合类。
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
"""
语法：namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):
typename:通过namedtuple创建的一个元组的子类的类名，通过这样的方式以初始化各种各样的实例化元组对象。
field_name: 类似于字典的key，在这里定义的元组可以通过这样的key去获取里面对应索引位置的元素值，这样的key可以是列表，也可以是用空格、/和逗号这样的分隔符隔开的字符串。
rename：如果rename指定为True，那么你的field_names里面不能包含有非Python标识符，Python中的关键字以及重复的name，
        如果有，它会默认给你重命名成‘_index’的样式，这个index表示该name在field_names中的索引，例：['abc', 'def', 'ghi', 'abc'] 将被转换成['abc', '_1', 'ghi', '_3']
"""
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

# 判断
print(isinstance(p, Point))
print(isinstance(p, tuple))

# deque使用list存储数据时,按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
from collections import defaultdict

# 对象
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)  # dict的key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # OrderedDict的key是有序的

# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od.keys())

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
from collections import OrderedDict


class LastUpdatedOrdereDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrdereDict, self).__init__()
        self._capacity = capacity

    # 该方法应该按一定的方式存储和key相关的value,在设置类实例属性时自动调用的.不能在该方法内赋值 self.name = value 会死循环
    def __setitem__(self, key, value):
        # self表示创建类实例本身,可以把各种属性绑定到self,因为self就指向创建实例的本身.
        # 判断key是不是类实例本身，是返回1(True)不是返回0(False)
        print(self)
        containsKey = 1 if key in self else 0
        print(len(self))
        print(self._capacity)
        if len(self) - containsKey >= self._capacity:
            # popitem 从字典中删除并返回键值对, 设置last为False,按照FIFO顺序返回对.默认为True
            last = self.popitem(last=False)
            print('remove:', last)
        # 判断containsKey是否为True，为True则删除key
        if containsKey:
            del self[key]
            print('set', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


FIFO = LastUpdatedOrdereDict(2)
FIFO.__setitem__('name', 'wangwu')
FIFO.__setitem__(1, 1)
FIFO.__setitem__(2, 2)
FIFO.__setitem__(3, 3)

# ChainMap
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。
# 什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。
# 我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。
from collections import ChainMap
import os, argparse

# 构造缺省参数：
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数：
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数：
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

"""
没有任何参数时，打印出默认参数：

$ python3 xxx.py 
color=red
user=guest
当传入命令行参数时，优先使用命令行参数：

$ python3 xxx.py  -u bob
color=red
user=bob
同时传入命令行参数和环境变量，命令行参数的优先级较高：

$ user=admin color=green python3 xxx.py  -u bob
color=green
user=bob
"""

# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
# 也可以update
c.update('hello')
print(c)
# Counter实际上也是dict的一个子类，上面的结果可以看出每个字符出现的次数。


# base64
"""
base64是一种用64个字符来表示任意二进制数据的方法.

用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，
所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。

Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
"""

# Python内置的base64可以直接进行base64的编解码：
import base64
base = base64.b64encode(b'binary\x00string')
print(base)

base1 = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(base1)
# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

base = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(base)
base = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(base)
base = base64.urlsafe_b64decode('abcd--__')
print(base)








