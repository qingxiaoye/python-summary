# !/usr/bin/python
# -*- coding:utf-8 -*-
import codecs
import os
import subprocess

import wget

with codecs.open('audio.txt', "r", "utf-8") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        file_name = wget.download(lines[i][:89], out=os.path.join(r'F:\yjcloud-learn\python-summary\audio', lines[i][53:89]))

