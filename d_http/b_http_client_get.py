# !/usr/bin/python
# -*- coding:utf-8 -*-
import http.client
import json

api_host = '127.0.0.1'
api_port = 9797
timeout = 10
f_url = '/api/v1/choice/opt-priv/user-dept-all'
headers = {
    "Content-Type": "application/json",
}
conn = http.client.HTTPConnection(api_host, api_port, timeout)
conn.request("GET", f_url,  headers=headers)

resp = conn.getresponse()
data = resp.read()
print(data)
# json_data = json.loads(data.decode("utf-8"))
# data = json_data['data']
# conn.close()
# print(data)
