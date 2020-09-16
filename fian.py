# !/usr/bin/python
# -*- coding:utf-8 -*-
import codecs
from datetime import datetime, timedelta
import os
import subprocess


def _obtain_timestamp():
    '''
    all the timestamp round to unit of day
    '''
    _limit_time = datetime.now()
    _hour, _minute, _second = datetime.now().strftime('%H:%M:%S').split(':')
    limit_time = datetime(_limit_time.year, _limit_time.month, _limit_time.day,
                          int(_hour), int(_minute), int(_second))

    week_time = _limit_time - timedelta(weeks=1)
    month_time = _limit_time - timedelta(days=30)
    quarter_time = _limit_time - timedelta(days=90)

    return [limit_time, week_time, month_time, quarter_time]


ct_list = _obtain_timestamp()
print(ct_list)
for ct_name, ct in zip(['week', 'month', 'quarter'], ct_list[1:]):
    print(ct_name, ct)
