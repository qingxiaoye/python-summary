# !/usr/bin/python
# -*- coding:utf-8 -*-
import time
import datetime
from dateutil.relativedelta import relativedelta
from datetime import date, datetime

print(datetime.strptime('2020-02', "%Y-%m") + relativedelta(months=+1))


def str2time(datetime_v):
    return datetime.strptime(datetime_v, "%Y-%m-%d")


def get_cur_next_month():
    cur_day_str = date.today().strftime("%Y-%m-%d")
    next_month_str = (str2time(cur_day_str) + relativedelta(months=+1)).strftime("%Y-%m")
    cur_month_str = date.today().strftime("%Y-%m")
    return cur_month_str, next_month_str


print(get_cur_next_month())
