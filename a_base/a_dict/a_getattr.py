# !/usr/bin/python
# -*- coding:utf-8 -*-
class Person:
    name = "Bill"
    age = 63
    country = "USA"


el_list = ['name', 'age', 'country']
for el in el_list:
    values = getattr(Person, el)
    print(values)
# print Person.age
# 如果属性存在，对属性重新赋值：
setattr(Person, 'age', 0)
# 如果属性不存在会创建一个新的对象属性，并对属性赋值：

