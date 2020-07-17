# -*- coding:utf-8 -*-

# from asd.get_audio_url import get_audio_urls, logger

from models import db_models, save_to_mysql
from models.sqlalchemy_mgr import SqlalchemyMgr
from libs.global_logger import get_logger

logger = get_logger(__name__)


def handle_audio(audio_file):
    try:
        print(audio_file)
        traffic_table_name = db_models.QiInfoTraffic.__tablename__
        query_sql = "select * from  {traffic_table_name} ".format(traffic_table_name=traffic_table_name)
        result=SqlalchemyMgr.Instance().query_sql(query_sql)
        logger.info("result is: %s", result)




    except Exception as exp:
        logger.error("error message: %s", exp)
