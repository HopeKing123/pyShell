# chardet:用于检测编码
# chardet支持检测的编码列表: https://chardet.readthedocs.io/en/latest/supported-encodings.html
import chardet
c = chardet.detect(b'Hello,world!')
print(c)
# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。

# 检测GBK编码的中文
data = '海阔凭鱼跃，天高任鸟飞'.encode('gbk')
d = chardet.detect(data)
print(d)
# 检测的编码是GB2312，注意到GBK是GB2312的超集，两者是同一种编码，检测正确的概率是74%，language字段指出的语言是'Chinese'。

# 对UTF-8编码进行检测：
data = '海阔凭鱼跃，天高任鸟飞'.encode('utf-8')
d = chardet.detect(data)
print(d)

# 对日文进行检测：
data = 'アリガド'.encode('utf-8')
d = chardet.detect(data)
print(d)

# 用chardet检测编码，使用简单。获取到编码后，再转换为str，就可以方便后续处理。
