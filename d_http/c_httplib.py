# !/usr/bin/python
# -*- coding:utf-8 -*-
import httplib
import urllib


def sendhttp():
    data = urllib.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = httplib.HTTPConnection('bugs.python.org')
    conn.request('POST', '/', data, headers)
    httpres = conn.getresponse()
    print(httpres.status)
    print(httpres.reason)


if __name__ == '__main__':
    sendhttp()
