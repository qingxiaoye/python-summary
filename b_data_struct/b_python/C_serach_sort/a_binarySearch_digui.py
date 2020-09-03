# !/usr/bin/python
# -*- coding:utf-8 -*-
def binarySearch(sort_list, item):
    if len(sort_list) == 0:
        return False, None
    else:
        mid = len(sort_list) // 2
        if item == sort_list[mid]:
            return True
        else:
            if item > sort_list[mid]:
                return binarySearch(sort_list[mid + 1:], item)
            else:
                return binarySearch(sort_list[:mid], item)


print(binarySearch([0, 1, 3, 5, 7, 9], 3))
