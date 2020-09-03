# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
类产生该类的对象(类的实例对象)，实例对象具有这个类所描述的行为

__init__
    初始化方法，构造本类的新对象
"""


class Student():
    counter = 0

    def __init__(self, age):
        self.age = age
        self.role = self._gcd(age)
        Student.counter += 1

    """
    静态方法的参数列表里面不应该有self参数
            加staticmethod
            局部使用的函数
    """

    @staticmethod
    def _gcd(age):
        if age > 10:
            return '青少年'
        else:
            return '成年'
    """
    类方法：
        实现与本类的所有对象有关的操作
        通过类实例调取该方法，
    """
    @classmethod
    def get_count(cls):
        return Student.counter


s1 = Student(age=10)
s2 = Student(age=10)
print(s1.role)

print(s1.counter)
print(Student.get_count())
