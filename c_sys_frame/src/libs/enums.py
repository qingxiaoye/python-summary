# -*- coding: utf-8 -*-
from enum import Enum

class TrafficFileStatusEnum(Enum):
    NO_FILE_HANDLE = 0  # 未处理
    FILE_PREPROCESS_FINISH = 1  # 预处理完成
    FILE_TRANSLATION_FINISH = 2  # 转译完成
    FILE_QUALITY_FINISH = 3  # 质检完成
    FILE_REVIEW_FINISH = 4  # 已复核
