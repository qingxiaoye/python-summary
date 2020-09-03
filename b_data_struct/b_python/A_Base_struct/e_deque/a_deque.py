# !/usr/bin/python
# -*- coding:utf-8 -*-
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addRight(self, item):
        self.items.append(item)

    def addLeft(self, item):
        self.items.insert(0, item)

    def removeRight(self):
        return self.items.pop()

    def removeLeft(self):
        return self.items.pop(0)


if __name__ == '__main__':
    d = Deque()
    d.addLeft(10)
    d.addLeft(9)
    d.addRight(11)
    print(d.items)
    print(d.removeLeft())
    print(d.removeRight())
