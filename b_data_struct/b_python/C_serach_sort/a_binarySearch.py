# !/usr/bin/python
# -*- coding:utf-8 -*-
def binarySearch(sort_list, item):
    first = 0
    last = len(sort_list)
    found = False
    item_index = None
    while not found and first < last:
        mid = (first + last) // 2
        print(mid)
        if item == sort_list[mid]:
            found = True
            item_index = mid
        else:
            if item > sort_list[mid]:
                first = mid + 1
            else:
                last = mid - 1

    return found, item_index


print(binarySearch([0, 1, 2, 3, 4, 5], 9))
