# !/usr/bin/python
# -*- coding:utf-8 -*-
# format
format_x = "{} is g {}".format('xqq', 'girl')
format_y = "{name} is g {attr}".format(name='xqq', attr='girl')

# split 和 rsplit

v_key = 'vc_name_xqq'
# 一个从左开始
print(v_key.split('_', 1))
# 一个从右开始
print(v_key.rsplit('_', 1))
print(v_key.split('_', 2))
