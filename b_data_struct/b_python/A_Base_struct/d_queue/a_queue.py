# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
insert函数向队列的尾部添加新元素
pop则可用于移除队列头部的元素（列表中的最后一个元素）
"""


class Queue:
    def __init__(self):
        self.items = []

    # 在队列的尾部添加一个元素
    def enqueue(self, item):
        self.items.insert(0, item)

    # 从队列的头部移除一个元素
    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.items)
    print(q.dequeue())
