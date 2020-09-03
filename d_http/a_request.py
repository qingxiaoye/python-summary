# !/usr/bin/python
# -*- coding:utf-8 -*-

import requests

url = 'https://s.call123.net:8443/cds/agent!statusun.net:9104/cds/agent!status?entId=7008000&passId=yj1635&startTime=20200731120000&endTime=20200801120000'
Response_get = requests.get(url)
print(Response_get.status_code)
print(Response_get.url)
print(Response_get.text)

# url = 'http://httpbin.org/post'
# d = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post(url, data=d)


