# !/usr/bin/python
# -*- coding:utf-8 -*-
from collections import defaultdict

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]


def intersect(nums1, nums2):
    m_dict = defaultdict(int)
    for i in nums1:
        m_dict[i] += 1
    k = 0
    for j in nums2:
        if m_dict[j] > 0:
            m_dict[j] += -1
            nums2[k] = j
            k += 1
    return nums2[0:k]


print(intersect(nums1, nums2))
