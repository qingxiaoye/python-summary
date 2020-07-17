# !/usr/bin/python
# -*- coding:utf-8 -*-
import sys
from datetime import datetime, time
import os
from apscheduler.schedulers.blocking import BlockingScheduler

from apscheduler.jobstores.memory import MemoryJobStore


class RunLogParser(object):

    def __init__(self, process_path, parser_start_time, parser_end_time):
        print(process_path, parser_start_time, parser_end_time)
        self.process_path = process_path

    def main(self):
        print(self.process_path)


def ff():
    xx = 'xxx'


if __name__ == '__main__':
    start_time = 123
    end_time = 456

    scheduler = BlockingScheduler()
    process_path = 'xxxxxxxxxx'
    x = RunLogParser('xqq', start_time, end_time)
    scheduler.add_job(x.main, 'cron', hour=10, minute=15)
    scheduler.start()
