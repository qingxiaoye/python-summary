# !/usr/bin/python
# -*- coding:utf-8 -*-
class Animal():
    cprop = "我是类上的属性cprop"

    def __init__(self, name, speed):
        self.name = name  # 动物名字
        self._speed = speed  # 动物行走或飞行速度

    def getSpeedBehavior(self):
        pass


class Cat(Animal):
    def __init__(self, name, speed, color, genre):
        super().__init__(name, speed)
        self.color = color
        self.genre = genre

    # 重写方法
    def getSpeedBehavior(self):
        print('running speed of %s is %s' % (self.name, self._speed))
        return self._speed


class Bird(Animal):
    def __init__(self, name, speed, color, genre):
        super().__init__(name, speed)
        self.color = color
        self.genre = genre

    # 重写方法
    def getSpeedBehavior(self):
        print('flying speed of %s is %s' % (self.name, self._speed))
        return self._speed


import time


class Manager:
    # 多态animal
    def __init__(self, animal):
        self.animal = animal

    def recordTime(self):
        self.animal.getSpeedBehavior()


if __name__ == "__main__":
    jiafeimao = Cat('cat', 2, 'gray', 'CatGenre')
    haiying = Bird('bird', 40, 'blue', 'BirdGenre')

    Manager(jiafeimao).recordTime()
    print('#' * 30)
    Manager(haiying).recordTime()
