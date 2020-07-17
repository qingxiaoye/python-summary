# !/usr/bin/python
# -*- coding:utf-8 -*-
import codecs
import subprocess

with codecs.open('audio.txt', "r", "utf-8") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        find_cmd_old = 'wget {dudio}'.format(dudio=lines[i][:89])
        print(find_cmd_old)
        cmd_result = subprocess.call([find_cmd_old], shell=True)
        if cmd_result!=0:
            find_cmd_old= 'no  {dudio} >>xqq.txt'.format(dudio=lines[i][:89])
            subprocess.call([], shell=True)
