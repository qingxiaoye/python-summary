# !/usr/bin/python
# -*- coding:utf-8 -*-
from mmap import mmap


def get_lines(fp):
    with open(fp, "r+") as f:
        m = mmap(f.fileno(), 0)
        print(m)
        tmp = 0
        for i, char in enumerate(m):
            print(i,char)
            if char == b"\n":
                yield m[tmp:i + 1].decode()
                tmp = i + 1


if __name__ == '__main__':
    for i in get_lines(r"text.txt"):
        pass
