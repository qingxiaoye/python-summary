# -*- coding:utf-8 -*-
import subprocess
import sys

import os

import Logging
import config
import db_models
import save_to_mysql
from comm import LogType
from sqlalchemy_mgr import SqlalchemyMgr

reload(sys)
sys.setdefaultencoding('utf8')


def check_store():
    Logging.logger.debug("Check Store start.")
    try:
        config_items = config.ConfigInfo.get_instance().get_config_items()
        max_store_size = config_items['MaxStoreSize'] * 1024 * 1024 * 1024  # 单位：B
        Logging.logger.debug(
            'check_store, max store size:  %s 字节( = %s M)( = %s G)。', str(max_store_size),
            config_items['MaxStoreSize'] * 1024, config_items['MaxStoreSize'])
        check_path = config_items['DstWavDir']
        # max_store_size = 2 * 1024 * 1024 * 1024  # 单位：B
        # check_path = '/home/user/wangfc/pythonProjects/remote_new_log_parser/input_data/dstWavDir'
        Logging.logger.debug('check_store, check path: %s, max store size: %s。', check_path, str(max_store_size))

        store_size = get_total_store(check_path)
        if store_size is None:
            Logging.logger.error('check_store, get_total_store return None')
            return
        Logging.logger.debug(
            'check_store, 目前占用 %s 字节( = %s M)( = %s G)。', str(store_size), str(store_size / (1024 * 1024)),
            str(store_size / (1024 * 1024 * 1024)))
        if store_size < max_store_size:
            Logging.logger.debug(
                'check_store, 还有 %s 字节( = %s M)( = %s G)可用。', str(max_store_size - store_size),
                str((max_store_size - store_size) / (1024 * 1024)),
                str((max_store_size - store_size) / (1024 * 1024 * 1024)))
            return
        Logging.logger.debug(
            'check_store, 存储空间已满，需要删除 %s 字节( = %s M)( = %s G)。', str(store_size - max_store_size),
            str((store_size - max_store_size) / (1024 * 1024),
                str((store_size - max_store_size) / (1024 * 1024 * 1024)))
        )
        delete_data(store_size - max_store_size)
    except Exception as exp:
        Logging.logger.error('check_store, error message：%s', exp)
    finally:
        Logging.logger.debug("Check Store finished.")

# 获取目录path的总大小，单位：字节
def get_total_store(path):
    try:
        cmd = "cd {path} && du -sb .".format(path=path)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out, err = p.communicate()
        line = out.splitlines()[0]
        return int(line.split('\t')[0])
    except Exception as exp:
        Logging.logger.error('get_total_store, error message：%s', exp)


def delete_data(store_size):
    Logging.logger.debug('delete_data, %s 字节数据待删除', str(store_size))
    try:
        query_sql = "select count(*) from {table} where type={type} and is_deleted=0".format(
            table=db_models.NgBakFile, type=LogType.AUDIO.value)
        query_result = SqlalchemyMgr.Instance().query_sql(query_sql)
        total_utterance_count = query_result[0][0]
        if total_utterance_count == 0:
            Logging.logger.debug('delete_data, bak_files中未删除的音频文件信息数量为0，无法进行数据删除。')
            return
        Logging.logger.debug('delete_data, bak_files中未删除的音频文件信息数量: %s.', total_utterance_count)

        sum_size, first, count = 0, 0, 1000
        delete_ids, path_list = list(), list()
        while sum_size < store_size and first <= total_utterance_count:
            query_sql = "select id, path, st_size from {table} where type={type} and is_deleted=0 ORDER BY origin_st_mtime limit {first}, {count}".format(
                table=db_models.NgBakFile, type=LogType.AUDIO.value, first=first, count=count)
            query_result = SqlalchemyMgr.Instance().query_sql(query_sql)
            query_sum = sum([item[2] for item in query_result])
            if sum_size + query_sum < store_size:
                delete_ids.extend([item[0] for item in query_result])
                path_list.extend([item[1] for item in query_result])
                sum_size += query_sum
                first += count
            else:
                for file_info in query_result:
                    delete_ids.append(file_info[0])
                    path_list.append(file_info[1])
                    if sum_size + file_info[2] >= store_size:
                        break
                    sum_size += file_info[2]
                break

        Logging.logger.debug("delete_data, delete file count：%s", len(path_list))
        for path in path_list:
            pcm_path, wav_path = path_list.split(";")
            if os.path.exists(pcm_path):
                os.remove(pcm_path)
            elif path and len(pcm_path):
                Logging.logger.debug("delete_data, file：%s is not exists", pcm_path)
            if os.path.exists(wav_path):
                os.remove(wav_path)
            elif path and len(wav_path):
                Logging.logger.debug("delete_data, file：%s is not exists", wav_path)

        save_to_mysql.del_multiple_data(delete_ids, db_models.NgBakFile)
    except Exception as exp:
        Logging.logger.error('delete_data, error message：%s', exp)

# if __name__ == '__main__':
# 	Logging.Logging.Instance().set_logger_config("debug", "/home/user/wangfc/pythonProjects/remote_new_log_parser/log")
# 	SqlalchemyMgr.Instance().connect('localhost', 3306, "root", "", "new_log_parser")
# 	check_store()
# 	delete_data(1073608532)
