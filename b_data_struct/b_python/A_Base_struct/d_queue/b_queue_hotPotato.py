# !/usr/bin/python
# -*- coding:utf-8 -*-
from A_Base_struct.d_queue.a_queue import Queue

"""
在模拟传土豆的过程中，程序将这个孩子的名字移出队列，然后立刻将其插入队列的尾部。
随后，这个孩子会一直等待，直到再次到达队列的头部。
在出列和入列num次之后，此时位于队列头部的孩子出局，新一轮游戏开始。
如此反复，直到队列中只剩下一个名字
"""


def hotPotato(nameList, num):
    q = Queue()
    for name in nameList:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


print(hotPotato(['F', 'E', 'D', 'C', 'B', 'A'], 7))
