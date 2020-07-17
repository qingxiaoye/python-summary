# !/usr/bin/python
# -*- coding:utf-8 -*-
from werkzeug.utils import secure_filename

filename='          a_a.py   '
print(secure_filename(filename))
print('a_a.py'.rsplit(".", 1))
print('a_a.py'.split('.',1))