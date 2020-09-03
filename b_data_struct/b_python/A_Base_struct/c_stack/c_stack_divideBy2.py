# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
10进制转2进制
    用2整除十进制整数，可以得到一个商和余数；
    再用2去除商，又会得到一个商和余数，
    如此进行，直到商为小于1时为止，然后把先得到的余数倒序排序，依次排列起来。
"""
from A_Base_struct.c_stack.c_stack import Stack


def divideBy2(decNumber):
    s = Stack()
    while decNumber > 0:
        s.push(decNumber % 2)
        decNumber = decNumber // 2
    binstring = ''
    while not s.isEmpty():
        binstring = binstring + str(s.pop())
    return binstring


print(divideBy2(233))
