# !/usr/bin/python
# -*- coding:utf-8 -*-


def num2str(num, base):
    convertstr = "0123456789ABCDEF"

    if num < base:
        return convertstr[num]
    else:
        return num2str(num // base, base) + convertstr[num % base]


print(num2str(10, 2))
