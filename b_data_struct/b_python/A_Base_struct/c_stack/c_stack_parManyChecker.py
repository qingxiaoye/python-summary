# !/usr/bin/python
# -*- coding:utf-8 -*-
from A_Base_struct.c_stack.c_stack import Stack


def parChecker(symbolString):
    """
    从左往右依次处理括号。
    如果遇到左括号，便通过push操作将其加入栈中，以此表示稍后需要有一个与之匹配的右括号。
    反之，如果遇到右括号，就调用pop操作
    """
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbolString) and balanced:
        if symbolString[index] in "{[(":
            s.push(symbolString[index])
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matchs(top, symbolString[index]):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matchs(open, close):
    opens = "{[("
    closes = "}])"
    return opens.index(open) == closes.index(close)


symbolString = "{()[{}]}"
print(parChecker(symbolString))
