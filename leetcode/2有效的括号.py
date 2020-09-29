# !/usr/bin/python
# -*- coding:utf-8 -*-
from collections import deque


class Solution:
    def isValid(self, s: str) -> int:
        brackets_dict = {'(': ')', '{': '}', '[': ']',"?":"?"}
        d = ['?']
        for s_i in s:
            if s_i in brackets_dict.keys():
                d.append(s_i)
            else:
                if brackets_dict[d.pop()] != s_i:
                    return False
            print(d)


if __name__ == '__main__':
    x = Solution()
    print(x.isValid('[)]{2}'))
