# -*- coding: utf-8 -*-
import collections
import os

import subprocess
from time import time
from datetime import date, timedelta
from datetime import datetime

import pandas as pd
import scandir


def current_timestamp_sec():
    # 1591349759
    return int(time())


def current_timestamp_ms():
    # ms的时间戳
    # 1591349860023
    return int(round(time() * 1000))


def current_datetime_sec():
    # 2020-06-05 17:37:17
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


print(current_timestamp_ms())


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result

    return timed


def datetime2timestamp(datetime_v):
    # python3
    # if not isinstance(datetime_v, datetime):
    #     return None
    # return int(time.mktime(datetime_v.timetuple()))

    # python3
    if isinstance(datetime_v, datetime):
        return int(datetime.timestamp(datetime_v))
    elif isinstance(datetime_v, date):
        return int(datetime.timestamp(datetime.combine(datetime_v, datetime.min.time())))
    else:
        return None


def get_default_date_interval(day_shift, today_shift=1):
    _today = date.today() + timedelta(days=today_shift)
    _shift_day = _today + timedelta(days=day_shift)

    return _shift_day, _today


def get_default_time_interval(day_shift):
    _now = datetime.now()
    _shift = (_now + timedelta(days=day_shift)).replace(hour=0, minute=0, second=0, microsecond=0, )

    return _shift, _now


def get_date_list(start_time, end_time):
    start_time = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d')
    end_time = datetime.fromtimestamp(end_time).strftime('%Y-%m-%d')
    date_list = [datetime2timestamp(x) for x in list(pd.date_range(start=start_time, end=end_time, freq='D'))]
    return date_list


def get_hour_list(start_time, end_time):
    start_time = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H')
    end_time = datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H')
    date_list = [datetime2timestamp(x) for x in list(pd.date_range(start=start_time, end=end_time, freq='H'))]
    return date_list


def exist_remote_file(file_path):
    """
    得curl工具存在

    :param file_path:
    :return:
    """
    command = 'curl --output /dev/null --silent --head --fail {}'.format(file_path)

    import subprocess as sp
    return_code = sp.call(command, shell=True)
    return return_code == 0


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def get_size_walk(root_path):
    """ 较慢，如果不用du，则使用scandir库，可以提高遍历性能 """
    if not os.path.exists(root_path):
        return None

    if os.path.isfile(root_path):
        if os.path.islink(root_path):
            return 0
        else:
            return os.path.getsize(root_path)

    if os.path.isdir(root_path):
        total_size = 0

        for dirpath, dirnames, filenames in os.walk(root_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    return None


def get_size_du(root_path):
    """ 只能用于linux环境 """
    # TODO du跟另外两种方法的结果有点出入
    return subprocess.check_output(['d', '-sb', root_path]).split()[0].decode('utf-8')


def get_size_scandir(root_path):
    if not os.path.exists(root_path):
        return None

    if os.path.isfile(root_path):
        if os.path.islink(root_path):
            return 0
        else:
            return scandir.stat(root_path).st_size

    if os.path.isdir(root_path):
        total_size = 0

        for dirpath, dirnames, filenames in scandir.walk(root_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    # total_size += os.path.getsize(fp)
                    total_size += scandir.stat(fp).st_size
        return total_size
    return None


# def symlink_force(target, link_name):
#     try:
#         os.symlink(target, link_name)
#     except OSError, e:
#         if e.errno == errno.EEXIST:
#             os.remove(link_name)
#             os.symlink(target, link_name)
#         else:
#             raise e


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def safe_cast_int(num_str, default=0):
    try:
        res = int(num_str)
        return res
    except:
        return default


def safe_cast_float(num_str, default=0., precision=None):
    try:
        res = float(num_str)
        if precision:
            res = round(res, precision)
        return res
    except:
        return default


def safe_division(dividend, divisor, default=0, precision=None):
    try:
        res = float(dividend) / float(divisor)
        if precision:
            res = round(res, precision)
        return res
    except:
        return default


def msec2time(num_str, default='00:00:00'):
    try:
        second = int(num_str)
        m, s = divmod(second / 1000, 60)
        h, m = divmod(m, 60)
        time = "%02d:%02d:%02d" % (h, m, s)
        return time
    except:
        return default
