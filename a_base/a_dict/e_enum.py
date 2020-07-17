# !/usr/bin/python
# -*- coding:utf-8 -*-
from enum import Enum

from aenum import MultiValueEnum, extend_enum


class ChoicesExItemEnum(Enum):
    ALL = 0  # 全有
    NEITHER = -1  # 全没有


class WkOrderServiceTypeME(MultiValueEnum):
    ALL = -1, "全部客服类型"
    ROBOT = 0, "机器人"
    MANUAL = 1, "人工客服"



print(ChoicesExItemEnum.ALL.value)
print(WkOrderServiceTypeME.ALL)
