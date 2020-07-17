# -*- coding:utf-8 -*-
import os
from asd.handle_audio import handle_audio

from libs.cfg_utils import get_config_dict
from libs.path_utils import get_project_dir
from libs.global_logger import get_logger
from models.sqlalchemy_mgr import SqlalchemyMgr


logger = get_logger(__name__)


class DataPreProcess(object):

    def __init__(self, audio_file):
        self.audio_file = audio_file
        project_dir = get_project_dir()
        config_file = os.path.join(project_dir, "cfg", "config.ini")
        # 配置路径检测
        if not isinstance(config_file, str):
            raise Exception('config file: {0} format is  not unicode.'.format(config_file))
        if not os.path.exists(config_file):
            raise Exception('config file: {0} is not exists.'.format(config_file))
        if not os.path.isfile(config_file):
            raise Exception('config file: {0} is not a file.'.format(config_file))
        db_info_dict = get_config_dict().get('MySQL', None)

        connect_result = SqlalchemyMgr.Instance().connect(db_info_dict.get('host', None),
                                                          db_info_dict.get('port', None),
                                                          db_info_dict.get('user', None),
                                                          db_info_dict.get('password', None),
                                                          db_info_dict.get('database', None))
        if not connect_result:
            logger.error("数据库连接失败，请检查数据库配置，程序退出.")
            exit(-1)

        # print('111')
        # print(SqlalchemyMgr.Instance().get_status())

    def data_process_handler(self):
        logger.info('Start Samples_Conversion')
        handle_audio(self.audio_file)

    def main(self):
        logger.info("Start Data_Pre_Process.")
        self.data_process_handler()


if __name__ == '__main__':
    audio_file = r"F:\yjcloud-learn\python-summary\b_sys_frame\data\001-a001-12345-1-2121-L001-y001-1589278505-10-80-aaa-1-sad12-ssdkosf12q1212131sd1212e44-F0012.V3"
    DataPreProcess(audio_file).main()



