# !/usr/bin/python
# -*- coding:utf-8 -*-


import time

"""
封装性
    __speed私有化
    私有属性，只能被 Animal3类 内的所有方法引用，如被方法getSpeed方法引用。
    但是，不能被其他类引用，也不能被 __str__ 引用
    AttributeError: 'Animal2' object has no attribute '_Manager__speed'
"""

class Animal3:
    def __init__(self, name, speed):
        self.name = name
        self.__speed = speed

    def getSpeed(self):
        print(self.__speed)

class Manager:
    def __init__(self, animal):
        self.animal = animal

    def recordTime(self):
        print('feeding time for %s（行走速度为:%s）  ' % (self.animal.name, self.animal.__speed))







cat = Animal3('加菲猫', 8)
cat.getSpeed()
xiaoming = Manager(cat)
xiaoming.recordTime()
 # AttributeError: 'Animal3' object has no attribute '_Manager__speed'
