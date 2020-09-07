# !/usr/bin/python
# -*- coding:utf-8 -*-
import threading  # 导入多线程模块


def eat():
    print('正在吃饭')
    print('线程名称 %s' % threading.current_thread().name)


def dance():
    print('正在跳舞')
    print('线程名称 %s' % threading.current_thread().name)


def song():
    print('正在唱歌')
    print('线程名称 %s' % threading.current_thread().name)


if __name__ == '__main__':

    thread = []  # 定义空列表用来保存线程
    t1 = threading.Thread(target=eat, args=(''))  # 定义第一条线程
    t2 = threading.Thread(target=dance, args=(''))  # 定义第二条线程
    t3 = threading.Thread(target=song, args=(''))  # 定义第三条线程
    thread.append(t1)  # 将线程依次加入到列表中
    thread.append(t2)
    thread.append(t3)
    for i in thread:
        i.start()  # 依次启动所有线程
    for i in thread:
        i.join()  # 守护所有线程
