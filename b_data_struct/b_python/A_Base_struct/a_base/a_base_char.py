# !/usr/bin/python
# -*- coding:utf-8 -*-
myName='Xiaoqq is a girl'


# count 计算item在字符串中出现的次数
myName.count('q')

"""
spilt
"""
v_key = 'vc_name_xqq_hello'

# 彻底切分
print(v_key.split('_'))
# ['vc', 'name', 'xqq', 'hello']

#  从左开始。 根据分割符逐个切割 x个
print(v_key.split('_', 1))
# ['vc', 'name_xqq_hello']
print(v_key.split('_', 2))
# ['vc', 'name', 'xqq_hello']

# 从右开始，根据分割符逐个切割 x个
print(v_key.rsplit('_', 1))
# ['vc_name_xqq', 'hello']
print(v_key.rsplit('_', 2))

"""
format
"""
format_x = "{} is g {}".format('xqq', 'girl')
format_y = "{name} is g {attr}".format(name='xqq', attr='girl')

"""
strip
"""
s = ' hello, world! '

print(s.strip())
print(s.lstrip(' hello, '))
print(s.rstrip('!'))



"""
字符串查找
index 找不到会报错
find 找不到会返回-1
"""
sStr1 = 'strchr'
sStr2 = 'st'
nPos = sStr1.index(sStr2)
print(nPos)
sStr1 = 'abcdefg'
sStr2 = 'h'
print(sStr1.find(sStr2))

"""
字符串倒序排列
"""
sStr1 = 'abcdefg'
sStr1 = sStr1[::-1]
print(sStr1)