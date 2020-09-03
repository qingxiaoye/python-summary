# !/usr/bin/python
# -*- coding:utf-8 -*-
import jieba.posseg as psg

sent = '今天中文分词是文本处理中不可缺少的一步123。pkq'
seg_list = psg.cut(sent)
print(seg_list)
# x=" ".join(['1','1'])
# print(x)
x=[(w,s) for w,s in seg_list]
print(x)