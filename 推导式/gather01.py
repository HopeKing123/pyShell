# 集合推导式(自动去重)：{}
list1 = [1, 2, 1, 3, 5, 2, 1, 8, 9, 7]

set1 = {x for x in list1}
print(set1)

# 判断大于5的
set2 = {x for x in list1 if x > 5}
print(set2)

