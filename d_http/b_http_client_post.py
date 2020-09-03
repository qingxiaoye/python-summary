# !/usr/bin/python
# -*- coding:utf-8 -*-
import http.client
import json
import urllib.parse

api_host = '127.0.0.1'
api_port = 9797
timeout = 10

f_url = "/api/v1/dept/test"
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded",
# }
headers = {'Content-type': 'application/json'}

data = {'n_dept_id': 1,
        'vc_name': "你好啊",
        "page": 1,
        "limit": 10}
json_data = json.dumps(data)

conn = http.client.HTTPConnection(api_host, api_port, timeout)
conn.request("POST", f_url, body=json_data, headers=headers)

resp = conn.getresponse()
data = resp.read()
print(data)
# data = json_data['data']
# print(data)
