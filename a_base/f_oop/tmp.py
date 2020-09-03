# !/usr/bin/python
# -*- coding:utf-8 -*-

class Animal():
    cprop = "我是类上的属性cprop"

    def __init__(self, name, speed):
        self.name = name  # 动物名字
        self.__speed = speed  # 动物行走或飞行速度

    def __str__(self):
        return '''Animal({0.name},{0.__speed}) is printed
                name={0.name}
                speed={0.__speed}'''.format(self)
    def getSpeed(self):
        return self.__speed
cat =Animal('cat1',10)
print(cat.getSpeed())