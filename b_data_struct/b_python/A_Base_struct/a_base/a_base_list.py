# !/usr/bin/python
# -*- coding:utf-8 -*-
myList1 = [0] * 6
# [0, 0, 0, 0, 0, 0]
myList2 = [[0]] * 3
# [[0], [0], [0]]

# Python列表提供的方法
myList = [1, 2, 3, 4]

myList.append(5)

myList.extend([1, 2, 3])

myList.insert(2, 10)

# 删除列表第i个元素，并返回删除的元素的值
myList.pop(1)

# 删除列表最后一个元素，并返回删除的元素的值
myList.pop()

# 移除列表中第一次出现的item
myList.remove(10)

myList.sort(reverse=False)

# 返回在item第一次出现的下标 如果包含start和stop，则在这个区间的
myList.index(1, 1)

# copy
# 和“=”区别
X1=myList.copy()
X1.append(10)

# item在list中出现的次数
print(myList.count(1))