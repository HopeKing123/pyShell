# 字典推导式
dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}
# 将key和value顺序颠倒,字典中的值是唯一的。所以会拿后面的值覆盖前面的值
newdict = {value: key for key, value in dict1.items()}
print(newdict)
