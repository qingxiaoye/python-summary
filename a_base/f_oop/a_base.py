# !/usr/bin/python
# -*- coding:utf-8 -*-
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat = Animal('加菲猫', 8)
print(cat)


# <__main__.Animal object at 0x000001CC4DC769B0>


class Animal2:
    def __init__(self, name, speed):
        self.name1 = name
        self.speed = speed

    """
    # 系统(又称为魔法)函数__str_
    # 可以打印
    # 使用0.数据名称的格式，这是类专有的打印格式
    """
    def __str__(self):
        # speed
        return "name is {0.name}--- speed is {0.speed}".format(self)


# 为实例添加属性，
# 只能对该实例添加属性，并不能改变类或其他实例
cat2 = Animal2('加菲猫', 8)
print(cat2)
# #
# cat2.color = 'red'
# print(getattr(cat2, 'color', None))
# # 判断某个对象是否有某个属性
# print(hasattr(cat2, 'XX'))
