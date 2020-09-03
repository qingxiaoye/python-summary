# -*- coding:utf-8 -*-
import subprocess
import uuid

import os
import scandir
import time
from enum import Enum


def get_uuid():
    guid = uuid.uuid4()
    return str(guid).replace('-', '')


def current_timestamp_sec():
    return int(time.time())


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
    return subprocess.check_output(['du', '-sb', root_path]).split()[0].decode('utf-8')


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


# if __name__ == '__main__':
#     # print get_size_scandir('/home/user/hezw/sc-redis')
#     print get_size_scandir('/home/admin/online_label_system/label_data')
#     # print get_size_du('/home/admin/online_label_system/label_data')
#     # print get_size_walk('/home/admin/online_label_system/label_data')


