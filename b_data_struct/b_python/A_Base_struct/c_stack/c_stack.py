# !/usr/bin/python
# -*- coding:utf-8 -*-
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    # 顶部元素
    # peek()返回栈顶端的元素，但是并不移除该元素。它不需要参数，也不会修改栈的内容。
    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(0)
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.items)
    print(s.pop())
    print(s.peek())
    print(s.size())
