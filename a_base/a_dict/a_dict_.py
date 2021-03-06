# !/usr/bin/python
# -*- coding:utf-8 -*-
from collections import Counter, defaultdict, OrderedDict
from operator import itemgetter
"""
Counter
"""
x = {"name": 4, "num": 370, "age": 370}
y = {"name": 2, "num": 14}

print(dict(Counter(x) + Counter(y)))
# char计数
count_el = Counter('hello world')
print(count_el)
# 对list计数
count_list = Counter([1, 2, 3, 3])
print(dict(count_list))
# 获取元素
print(list(count_list.elements()))

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

dict_1 = defaultdict(list)

for _k, _v in s:
    dict_1[_k].append(_v)

d5 = OrderedDict()
for _k, _v in s:
    d5[_k] = _v
print(d5)

print('*' * 10)

dict1 = {'a': 7, 'b': 5}

"""
sorted 
"""
print('对字典排序')

# 对字典排序。按照values值倒序排序，返回的只有keys
tag = sorted(dict1, key=dict1.__getitem__, reverse=True)
print('tag',tag)

# 对字典排序。按照values值倒序排序，返回完整字典list
tag2 = sorted(dict1.items(), key=itemgetter(0), reverse=True)
print(tag2)

sorted_results = sorted(dict1.items(), key=lambda item: item[0], reverse=True)  # list
print(sorted_results)


x=(241, 253, 81, 72, 80, 74, 71, 254, 252, 304, 306)
y=(71, 72, 74, 76, 80, 81, 241, 246, 247, 250, 251, 252, 253, 254, 296, 297, 298, 299, 300, 301, 302, 303)
print(x^y)