# !/usr/bin/python
# -*- coding:utf-8 -*-
import re

text_string = '文本最重要的来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。' \
              '利用一个爬虫抓取到网络中的信息。爬取的策略有广度爬取和深度爬取。' \
              '根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。'
# ^text 以text开头
regex = '^文本'
p_string = text_string.split('。')  # 以句号为分隔符通过split切分
"""
search
"""
for line in p_string:
    if re.search(regex, line) is not None:  # search方法是用来查找匹配当前行是否匹配这个regex，返回的是一个match对象
        print(line)  # 如果匹配到，打印这行信息

"""
findall 
返回匹配的结果
"""

year_string = '2019年12月'
regex = '[1-9]\d{4}'
year = re.findall(regex, year_string)
print(year)
