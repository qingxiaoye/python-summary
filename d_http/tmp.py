# !/usr/bin/python
# -*- coding:utf-8 -*-
import http.client
import json
import urllib.parse

data='[{"recipient_id":"default","text":"\u548b\u4e86\uff0c\u53ef\u4ee5\u544a\u8bc9\u6211\u5417"}]'
xx= data.encode('utf-8').decode('unicode_escape')
print(xx)