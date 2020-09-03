# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
lamada
     需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
"""
from functools import reduce


def sum_two(x, y):
    return x + y


# lamada相当于上面的函数
add = lambda x, y: x + y

# 常用的方法
list1 = [3, 5, -4, -1, 0, -2, -6]
list2 = sorted(list1, key=lambda x: abs(x))

"""
map(func, *iterables)
    传入的第一个参数是f，map将f依次作用到序列的每个元素，并把结果作为新的Iterator返回
"""

x = map(lambda x: x * x, list1)
print(list(x))
"""
reduce
    reduce把f作用在一个序列[x1, x2, x3, ...]上，f必须接收两个参数。
"""
list1 = [3, 5, -4, -1, 0, -2, -6]

x = reduce(lambda x, y: x + y, list1)
print(x)

# map作用将序列s中每一个字符转化为num，返回一个Iterator对象
# ，reduce的参数fn将这个Iterator对象转化为对应的整数表示。
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


def fn(x, y):
    return x * 10 + y


x = reduce(fn, map(char2num, '123456'))
print(x)
