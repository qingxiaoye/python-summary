# -*- coding:utf-8 -*-
import datetime
import sys
import os


def get_project_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))


def get_src_dir():
    return os.path.join(get_project_dir(), 'src')


def get_resource_dir():
    return os.path.join(get_src_dir(), 'resource')


def get_package_path():
    dirname_list = [dirname for dirname in sys.path if 'site-packages' in dirname]
    return os.path.abspath(dirname_list[0]) if len(dirname_list) > 0 else None


def get_file_path(file_path):
    (filepath, tempfilename) = os.path.split(file_path)
    return filepath


def get_file_name(file_path):
    (filepath, tempfilename) = os.path.split(file_path)
    (filename, extension) = os.path.splitext(tempfilename)
    return filename


def get_file_format(file_path):
    (filepath, tempfilename) = os.path.split(file_path)
    (filename, extension) = os.path.splitext(tempfilename)
    return extension


def get_file_exte(file_path):
    (filepath, file_exte) = os.path.split(file_path)
    return file_exte


def get_date_dir():
    cur_year = str(datetime.datetime.now().year)
    cur_month = str(datetime.datetime.now().month)
    cur_day = str(datetime.datetime.now().day)
    cur_date_dir = os.path.join(cur_year, cur_month, cur_day)
    return cur_date_dir
