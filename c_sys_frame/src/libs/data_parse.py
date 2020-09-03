# -*- coding:utf-8 -*-
import os
import time
import pygrok
from models import save_to_mysql, db_models
from libs.global_logger import get_logger
from libs.path_utils import get_file_name

logger = get_logger(__name__)

def audio_parse(text):
    pattern = "%{WORD:SetVar}-%{WORD:traffic_record_number}-%{WORD:agent_id}" \
        + "-%{WORD:extension_number}-%{WORD:call_direction}-%{WORD:calling_number}" \
        + "-%{WORD:called_number}-%{WORD:call_start_time}-%{WORD:duration}-%{WORD:satisfaction}" \
        + "-%{WORD:recording_id}-%{WORD:track}-%{WORD:original_project}-%{WORD:call_id}-%{WORD:file_name}"

    grok = pygrok.Grok(pattern)
    try:
        audio_info_dict = grok.match(text)
        SetVar = audio_info_dict['SetVar']
        traffic_record_number = audio_info_dict['traffic_record_number']
        agent_id = audio_info_dict['agent_id']
        extension_number = int(audio_info_dict['extension_number'])
        call_direction = int(audio_info_dict['call_direction'])
        calling_number = audio_info_dict['calling_number']
        called_number = audio_info_dict['called_number']
        call_start_time = int(audio_info_dict['call_start_time'])
        duration = int(audio_info_dict['duration'])
        satisfaction = int(audio_info_dict['satisfaction'])
        recording_id = audio_info_dict['recording_id']
        track = int(audio_info_dict['track'])
        original_project = audio_info_dict['original_project']
        call_id = audio_info_dict['call_id']
        file_name = audio_info_dict['file_name'] + '.wav'

        time_array = time.localtime(call_start_time)
        call_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)

        recording_info_dict = dict(insert_time=int(time.time()), is_deleted=0, recording_id=recording_id, call_id=call_id,
                                   file_name=file_name, track=track)
        traffic_info_dict = dict(insert_time=int(time.time()), is_deleted=0, call_id=call_id, original_project=original_project,
                                 traffic_record_number=traffic_record_number, agent_id=agent_id, extension_number=extension_number,
                                 call_direction=call_direction, calling_number=calling_number, called_number=called_number,
                                 call_start_time=call_start_time, duration=duration, satisfaction=satisfaction)
        insert_recording_info_dict_list = [recording_info_dict]
        insert_traffic_info_dict_list = [traffic_info_dict]
        save_to_mysql.save_dic_to_mysql(insert_recording_info_dict_list, db_models.QiInfoRecording)
        save_to_mysql.save_dic_to_mysql(insert_traffic_info_dict_list, db_models.QiInfoTraffic)

        return call_id, file_name
    except Exception as exp:
        logger.error("error message: %s", exp)


if __name__ == '__main__':
    from libs.cfg_utils import get_config_dict
    from libs.path_utils import get_project_dir
    from models.sqlalchemy_mgr import SqlalchemyMgr

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
    audio_file = "/home/user/001-a001-12345-1-2121-L001-y001-1589278505-10-80-aaa-1-sad12-ssdkosf12q1212131sd1212e43-F0011.wav"
    text = get_file_name(audio_file)
    _, file_name = audio_parse(text)