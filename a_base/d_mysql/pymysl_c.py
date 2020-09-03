# !/usr/bin/python
# -*- coding:utf-8 -*-
import pymysql
import pymysql as pymysql

db = pymysql.connect(host='192.168.108.197', port=3306, user='root', passwd='', db='brain_cr', charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
query_sql = "SELECT * from 12368gd  "
cursor.execute(query_sql)

# 使用 fetchone() 方法获取单条数据.
rows = cursor.fetchall()

vm_keys_wkcall = [
    'id',
    'vc_call_number',
    'session_id',
    'n_call_time',
    'vc_complain_user_url',
    'vc_judge_user_url',
    'vc_case_dsr_sfzh',
    'judge_ldr_sfzh',
    'complain_ldr_sfzh',
    'robot_case',
    'user_case',
    'vc_an_case_info',
    'robot_lawsuit',
    'user_lawsuit',
    'robot_court',
    'user_court',
    'vc_court_name',
    'robot_judge',
    'user_judge',
    'vc_judge_case_info',
    'robot_complain',
    'user_complain',

]

for row in rows:
    print(row.user_complain)
