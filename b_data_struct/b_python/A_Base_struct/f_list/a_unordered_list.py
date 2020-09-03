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


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            print(current.getData())
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if item == current.getData():
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if item == current.getData():
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.add(10)
    mylist.add(9)
    mylist.add(8)
    mylist.add(7)
    mylist.add(6)
    mylist.add(5)
    # print(mylist.length())
    # print(mylist.search(1000))
    mylist.remove(9)
    print(mylist.length())
