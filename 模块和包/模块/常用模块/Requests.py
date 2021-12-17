# requests:用于处理url
# requests常用方法：https://www.cnblogs.com/031602523liu/p/9817927.html
import requests,json

# get请求(无参)
r = requests.get('https://bilibili.com/')
print(r.status_code)
# 响应返回文本内容
# print(r.text)

# get请求(有参),params：字典或字节序列，作为参数增加到url中
r = requests.get('https://bilibili.com/', params={'q': 'python', 'cat': '1001'})
print(r.url)
# 检测编码
print(r.encoding)

# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
# print(r.content)

# 对特定类型响应,例如JSON
# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())

# 需要传入HTTP Header时，传入一个dict作为headers参数：
r = requests.get('https://www.bilibili.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)

# POST请求,data:字典，字节序列或文件对象，作为Request的内容
a = requests.post('https://mail.qq.com/', data={'form_email': 'xxxxxxx@qq.com', 'form_password': 'xxxxxxxxxx'})
print(a)

# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = ('key', 'value')
b = requests.post('https://mail.qq.com', json=params)

# 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
upload_files = {'file': open('report.xls', 'rb')}
c = requests.post('url', files=upload_files)

# 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

# requests获取HTTP响应的其他信息,例如：响应头
print(r.headers)
print(r.headers['Content-Type'])


# requests对Cookie做了特殊处理,可以轻松获取指定的Cookie
print(r.cookies['ts'])

# 在请求中传入Cookie,只需要准备一个dict传入cokies参数
cs = {'token': '12345', 'status': 'working'}
r = requests.get('url', cookies=cs)

# 指定超时，传入以秒为单位的timeout参数
r = requests.get('url',timeout=2.5)
































