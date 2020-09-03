# !/usr/bin/python
# -*- coding:utf-8 -*-
from A_Base_struct.e_deque.a_deque import Deque

"""
回文检测器
    回文是指从前往后读和从后往前读都一样的字符串
"""


def parChecker(astring):
    d = Deque()
    for item in astring:
        d.addRight(item)
    isTrue = True

    while d.size() > 1:
        first = d.removeLeft()
        right = d.removeRight()
        if first != right:
            isTrue = False
    return isTrue


if __name__ == '__main__':
    print(parChecker('asdsa'))
