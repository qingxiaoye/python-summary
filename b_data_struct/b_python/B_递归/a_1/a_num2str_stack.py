# !/usr/bin/python
# -*- coding:utf-8 -*-
from A_Base_struct.c_stack.c_stack import Stack

s1 = Stack()


def num2str(num, base):
    convertstr = "0123456789ABCDEF"

    if num < base:
        s1.push(convertstr[num])
    else:
        s1.push(convertstr[num % base])
        num2str(num // base, base)


num2str(255, 16)
string = ''
while not s1.isEmpty():
    string = string + s1.pop()
print(string)
