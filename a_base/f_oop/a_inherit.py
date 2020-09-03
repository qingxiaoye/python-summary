# !/usr/bin/python
# -*- coding:utf-8 -*-

"""
继承
子类继承父类的所有public和protected数据和方法，极大提高了代码的重用性
"""


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'

    def talk(self):
        print("{} is talking....".format(self.name))

    def speak(self):
        print("{} is speaking....".format(self.name))


class Chinese(Person):

    def __init__(self, name, age, language):  # 先继承，在重构
        # super().__init__(name, age)  # 继承父类的构造方法，也可以写成：super(Chinese,self).__init__(name,age)
        Person.__init__(self, name, age)
        self.language = language  # 定义类的本身属性

    def walk(self):
        print('{} is walking...'.format(self.name))

    def speak(self):  # 子类 重构方法
        print('%s is speaking chinese' % self.name)


c = Chinese('bigberg', 22, 'xqq')

# 继承方法
c.talk()

# # 继承属性
c.walk()

# 重构
c.speak()
