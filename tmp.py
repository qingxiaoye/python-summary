# !/usr/bin/python
# -*- coding:utf-8 -*-
from operator import itemgetter
import re

string = '查询到湖州中院的地址是浙江省湖州市吴兴区仁皇山路300' \
         '号请问你还需要什么其他帮助，继续查询该法院信息请说继续，查询其他法院信息请说其他，返回主菜单请说返回&您要查询哪所法院的信息，您可以查询湖州中院及其下属法院的信息&您想要咨询安吉法院什么信息呢？您可以咨询地址、邮编、办公时间、公交路线等&查询到安吉法院的地址是浙江省湖州市安吉县昌硕西路69号请问你还需要什么其他帮助，继续查询该法院信息请说继续，查询其他法院信息请说其他，返回主菜单请说返回&已返回主菜单，您可以进行案件查询，联系法官，法院信息查询，法律咨询，信访投诉与建议，有什么可以帮您？& '

pattern = '查询到[\u4E00-\u9FA5]{2,4}院的'
result_finditer = re.finditer(pattern, string, flags=0)
l_court=[]
for i in result_finditer:  # i 本身也是可迭代对象，所以下面要使用 i.group()
    l_court.append(i.group())
print(l_court)