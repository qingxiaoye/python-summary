# !/usr/bin/python
# -*- coding:utf-8 -*-
import numpy as np

A = np.arange(1, 5).reshape(1, 4)
B = np.arange(0, 4).reshape(1, 4)
print(np.multiply(A, B))  # 数组对应元素位置相乘
C = np.arange(0, 4).reshape(4, 1)
print(np.multiply(A,C))  # 数组对应元素位置相乘

# print(A * B)
# print(A * C)
# print(C * A)

# print(A)
# print(B[:, 0])
# print(np.multiply(A, B))  # 数组对应元素位置相乘
#
print((np.mat(A)) * (np.mat(C)))  # 执行矩阵运算
# print(A * B[:, 0])
