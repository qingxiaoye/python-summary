# !/usr/bin/python
# -*- coding:utf-8 -*-
import abc


class Animal:
    cprop = "我是类上的属性cprop"

    def __init__(self, name, speed):
        self.name = name  # 动物名字
        self._speed = speed  # 动物行走或飞行速度

    # 使用abstractmethod装饰器后，变为抽象方法
    @abc.abstractmethod
    def getSpeedBehavior(self):
        pass
