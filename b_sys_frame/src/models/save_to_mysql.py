# -*- coding:utf-8 -*-
"""
This module is used to save some objects to mysql.
This module contains some methods.
"""

import time

from libs.global_logger import get_logger
from models import sqlalchemy_mgr, db_models

logger = get_logger(__name__)


def save_dic_to_mysql(log_info_dic_list, module_class):
    if (log_info_dic_list is None) or (len(log_info_dic_list) == 0):
        return
    total_count = len(log_info_dic_list)
    logger.debug('向数据表%s中保存%s条数据', module_class.__tablename__, total_count)
    try:
        start_time = time.time()
        single_bulk = 30000
        session = sqlalchemy_mgr.SqlalchemyMgr.Instance().get_session()
        if session is None:
            logger.error("连接数据库出错, 写库失败")
            return False
        for chunk in range(0, total_count, single_bulk):
            sub_start_time = time.time()
            session.execute(
                module_class.__table__.insert().prefix_with("IGNORE"),
                log_info_dic_list[chunk:min(chunk + single_bulk, total_count + 1)]
            )
            session.commit()

            logger.debug("insert(ignore) into %s, count: %s, cost: %s seconds. ", module_class.__tablename__,
                         min(single_bulk, total_count - chunk), str(time.time() - sub_start_time))

        logger.debug("insert(ignore) into %s, count: %s, cost: %s seconds. ", module_class.__tablename__,
                     str(total_count), str(time.time() - start_time))
        return True
    except Exception as exp:

        logger.error("向数据表%s写入数据时出错, message: %s", module_class.__tablename__, exp )
        return False


def update_file_status_to_mysql(update_list):
    if update_list is None:
        logger.error("update_file_status_to_mysql: input update_list is None.")
    try:
        start_time = time.time()
        session = sqlalchemy_mgr.SqlalchemyMgr.Instance().get_session()
        single_bulk = 30000
        total_count = len(update_list)
        for chunk in range(0, total_count, single_bulk):
            sub_start_time = time.time()
            for i in range(chunk, min(chunk + single_bulk, total_count)):
                update_sql = "update {0} set related_status=1 where id={1}".format(
                    db_models.NgTransDelayInfo.__tablename__, update_list[i])
                session.execute(update_sql)
            session.commit()

            logger.debug("update %s, count: %s, cost: %s seconds. ", db_models.NgTransDelayInfo.__tablename__,
                         min(single_bulk, total_count - chunk), str(time.time() - sub_start_time))

        logger.debug("update %s, count: %s, cost: %s seconds. ", db_models.NgTransDelayInfo.__tablename__,
                     str(total_count), str(time.time() - start_time))
    except Exception as exp:

        logger.error("error message: %s", exp )
