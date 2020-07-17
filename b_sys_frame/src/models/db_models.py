# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, Index, String, text
from sqlalchemy.dialects.mysql import DATETIME, INTEGER, SMALLINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from libs.cfg_utils import get_config_dict

Base = declarative_base()
metadata = Base.metadata


class QiInfoTraffic(Base):
    __tablename__ = 'qi_info_traffic'

    insert_time = Column(INTEGER(11), server_default=text("'0'"))
    is_deleted = Column(SMALLINT(6), server_default=text("'0'"))
    id = Column(INTEGER(11), primary_key=True)
    call_id = Column(VARCHAR(64), unique=True)
    original_project = Column(VARCHAR(128), index=True)
    traffic_record_number = Column(VARCHAR(64))
    agent_id = Column(VARCHAR(64))
    extension_number = Column(VARCHAR(16))
    call_direction = Column(SMALLINT(6))
    calling_number = Column(VARCHAR(16))
    called_number = Column(VARCHAR(16))
    call_start_time = Column(DateTime)
    duration = Column(INTEGER(11))
    satisfaction = Column(INTEGER(11))
    file_status = Column(SMALLINT(6), index=True, server_default=text("'0'"))
    hit_status = Column(SMALLINT(6))
    review_status = Column(SMALLINT(6))
    appeal_status = Column(SMALLINT(6))


class QiInfoRecording(Base):
    __tablename__ = 'qi_info_recording'

    insert_time = Column(INTEGER(11))
    is_deleted = Column(SMALLINT(6), server_default=text("'0'"))
    id = Column(INTEGER(11), primary_key=True)
    recording_id = Column(String(64))
    call_id = Column(VARCHAR(64), unique=True)
    original_call_id = Column(VARCHAR(64))
    file_name = Column(VARCHAR(255))
    path = Column(VARCHAR(255))
    url = Column(String(255))
    track = Column(SMALLINT(6), index=True, comment='0£ºË«ÉùµÀ£»1-µ¥ÉùµÀ')


class QiPreprocessingRecording(Base):
    __tablename__ = 'qi_preprocessing_recording'

    insert_time = Column(INTEGER(11))
    is_deleted = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    id = Column(INTEGER(11), primary_key=True)
    file_name = Column(VARCHAR(255), nullable=False)
    path = Column(VARCHAR(255), nullable=False)
    url = Column(String(255), nullable=False)
    call_id = Column(VARCHAR(64), nullable=False, unique=True)
    channel_type = Column(SMALLINT(6), nullable=False)
    task_id = Column(VARCHAR(50), nullable=False)

class QiInfoRecallfile(Base):
    __tablename__ = 'qi_info_recallfile'

    insert_time = Column(INTEGER(11))
    is_deleted = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    id = Column(INTEGER(11), primary_key=True)
    url = Column(String(255), nullable=False)
    call_id = Column(VARCHAR(64), nullable=False, unique=True)