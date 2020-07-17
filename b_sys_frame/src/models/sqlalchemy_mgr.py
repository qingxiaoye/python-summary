# -*- coding:utf-8 -*-

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from libs.global_logger import get_logger

logger = get_logger(__name__)


class SqlalchemyMgr(object):
    __instance = None

    def __init__(self):
        self.__engine = None
        self.__session = scoped_session(sessionmaker())
        self.__connect_status = False

    @classmethod
    def Instance(cls):
        if cls.__instance is None:
            cls.__instance = SqlalchemyMgr()
        return cls.__instance

    def connect(self, host, port, user, password, database, charset='utf8'):
        try:
            # todo
            # backinfo = os.system('ping -c 1 -w 1 %s' % host)
            # print(backinfo)
            # if backinfo:
            #     logger.error('connect: ping %s 失败，请检查数据库配置。', host)
            #     return False
            conn_str = 'mysql+cymysql://{0}:{1}@{2}:{3}/{4}?charset={5}'.format(
                user, password, host, int(port), database, charset)
            print(conn_str)
            # 生成一个数据库引擎，echo=True 时，会显示每条执行的 SQL 语句，生产环境下应关闭
            self.__engine = create_engine(conn_str, echo=False)  # echo=True时，会打印每一条sql语句
            self.__session.remove()
            self.__session.configure(bind=self.__engine, autoflush=False, expire_on_commit=False)
            try:
                self.__engine.connect().execute('SELECT 1')
                self.__connect_status = True
                return True
            except Exception as connect_mysql_exp:
                logger.error('连接数据库失败, message: %s', connect_mysql_exp)
                self.__connect_status = False
                return False
        except Exception as exp:
            logger.error('连接数据库失败, message: %s', exp)
            return False

    def get_session(self):
        if self.__connect_status:
            try:
                self.__engine.connect().execute('SELECT 1')
                self.__connect_status = True
                return self.__session
            except Exception as connect_mysql_exp:
                logger.error('连接数据库失败, message: %s', connect_mysql_exp)
                self.__connect_status = False
                return
        else:
            logger.error('数据库未连接.')
            return

    def query_sql(self, sql_str):
        print('__connect_status',self.__connect_status)
        # if not self.__connect_status:
        #     raise Exception('数据库未连接.')
        try:
            data_query = self.__session.execute(sql_str)
            self.__session.commit()
            result = data_query.fetchall()
            logger.debug('execute query sql: %s, affected rows count: %d', sql_str, len(result))
            return result
        except Exception as exp:
            logger.error('execute query sql: %s, error message: %s', sql_str, exp)

    def update_sql(self, sql_str):
        if not self.__connect_status:
            raise Exception('数据库未连接.')
        try:
            data_query = self.__session.execute(sql_str)
            self.__session.commit()
            logger.debug('execute query sql: %s, affected rows count: %d', sql_str, data_query.rowcount)
            return True
        except Exception as exp:
            logger.error('execute query sql: %s, error message: %s', sql_str, exp)
            return False

    def execute_sql(self, sql_str):
        if not self.__connect_status:
            raise Exception('数据库未连接.')
        try:
            logger.debug('execute query sql: %s', sql_str)
            self.__session.execute(sql_str)
            self.__session.commit()
        except Exception as exp:
            logger.error('execute query sql: %s, error message: %s', sql_str, exp)

    def get_status(self):
        return self.__connect_status