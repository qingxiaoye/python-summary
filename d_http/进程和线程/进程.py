# !/usr/bin/python
# -*- coding:utf-8 -*-
# 导入多进程模块
import multiprocessing
import os


def target_func():
    print("子进程名字", multiprocessing.current_process().name)
    print("子进程PID：", os.getpid())
    print("子进程的父进程ppid:", os.getppid())


if __name__ == '__main__':

    for i in range(3):
        # 创建进程实例，指定要执行的目标函数
        p = multiprocessing.Process(target=target_func)
        p.start()  # 使用start方法启动进程
        p.join()  # 等待子进程结束
        print("主进程pid：", os.getpid())
