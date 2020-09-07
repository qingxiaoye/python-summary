# !/usr/bin/python
# -*- coding:utf-8 -*-
from operator import itemgetter

print(1, ' 对字典进行排序')
dict1 = {"a": 10, "b": 9, "d": 11}
# 默认正序排序即 revere=False
# lambda i: i[1]：为0对key排序，为1对value排序，
sort_dcit = sorted(dict1.items(), key=lambda i: i[1], reverse=True)
print(sort_dcit)
sort_dcit2 = sorted(dict1.items(), key=itemgetter(1), reverse=True)
print(sort_dcit2)
print('2 字典迭代式')
d = {key: value for (key, value) in dict1.items()}
print(d)
print('3 反转字符串')
x = 'abcde'
print(x[::-1])
print('4 将字符串 "k:1|k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}')
str1 = 'k:1|k1:2|k2:3|k3:4'
dict2 = {k: v for s in str1.split('|') for k, v in (s.split(':'),)}
print(dict2)
print("5 将字符串  abcde  处理成字典  ['a', 'b', 'c', 'd', 'e']")

str3 = 'abcde'
list2 = list(x)
print(list2)
# 函数的方法
dict3 = {}
for items in str1.split('|'):
    k, v = items.split(':')
    dict3[k] = v
print(dict3)
print('6 请按alist中元素的age由大到小排序')
alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]
sort_alist = sorted(alist, key=lambda x: x['age'])
print(sort_alist)
print('7 下面代码的输出结果将是什么？')
list1 = ['a', 'b', 'c', 'd', 'e']
print(list1[10:])  # []
# print(list1[10])  IndexError: list index out of range
print(list1[:10])  # ['a', 'b', 'c', 'd', 'e'

print('8 给定两个列表：找出相同的元素 、不同的元素、组合元素')
list1 = [1, 2, 3]
list2 = [3, 4, 5]
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)
print(set1 | set2)
print(set1 ^ set2)
print('9 删除list里面的重复元素并按照原先的顺序展现')
l1 = ['b', 'c', 'd', 'c', 'a', 'a']
l2 = sorted(set(l1), key=l1.index)
print(l2)
