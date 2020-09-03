# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
将整数转换成任意进制的字符串
10进制转任意base进制
    用base整除十进制整数，可以得到一个商和余数；
    再用base去除商，又会得到一个商和余数，
    如此进行，直到商为小于1时为止，然后把先得到的余数倒序排序，依次排列起来。
"""
from A_Base_struct.c_stack.c_stack import Stack


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"
    s = Stack()
    while decNumber > 0:
        s.push(decNumber % base)
        decNumber = decNumber // base
    binstring = ''
    while not s.isEmpty():
        binstring = binstring + digits[s.pop()]
    return binstring


print(baseConverter(999999, 16))
