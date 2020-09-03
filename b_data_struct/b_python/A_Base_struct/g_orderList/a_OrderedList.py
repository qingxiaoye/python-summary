# !/usr/bin/python
# -*- coding:utf-8 -*-
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:
    """
    header最小
    """

    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            print(current.getData(), item)
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        tmp = Node(item)
        if previous is None:
            tmp.setNext(self.head)
            self.head = tmp
        else:
            tmp.setNext(current)
            previous.setNext(tmp)

    def remove(self, item):
        pass

    def search(self, item):
        pass

    def index(self, item):
        pass

    def pop(self):
        pass

    def isEmpty(self):
        pass

    def length(self):
        pass


if __name__ == '__main__':
    odlist = OrderedList()
    odlist.add(10)
    odlist.add(12)
