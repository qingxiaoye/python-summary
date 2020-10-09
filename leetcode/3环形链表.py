# !/usr/bin/python
# -*- coding:utf-8 -*-


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mini_data = [math.inf]

    def push(self, x: int) -> None:
        self.data.append(x)
        self.mini_data.append(min(x, self.mini_data[-1]))

    def pop(self) -> None:
        self.data.pop()

        self.mini_data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mini_data[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    obj = MinStack()
    obj.push(10)
    obj.push(11)
    obj.pop()
    obj.pop()

    print(obj.getMin())
