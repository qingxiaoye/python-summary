# !/usr/bin/python
# -*- coding:utf-8 -*-
import sys

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def my_job1():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class RunLogParser(object):
    def main(self, parser_start_time):
        print(sys.argv[0])
        if parser_start_time is None:
            parser_start_time=my_job1()
            print(parser_start_time)


scheduler = BlockingScheduler()
RunParser = RunLogParser()
parser_start_time = None
scheduler.add_job(RunParser.main, 'cron', second='*/20' , replace_existing=True,
                  args=[parser_start_time])

# 每隔5秒运行一次my_job1
scheduler.start()
