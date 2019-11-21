"""
两个栈实现队列
执行用时 :56 ms, 在所有 python3 提交中击败了19.53%的用户
内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.08%的用户
"""


class MyQueue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x):
        if self.stack_1 is []:
            self.stack_1.append(x)
        else:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            self.stack_1.append(x)
            while self.stack_2:
                self.stack_1.append(self.stack_2.pop())
        return True

    def pop(self):
        if self.stack_1:
            return self.stack_1.pop()
        return False

    def peek(self):
        if self.stack_1:
            return self.stack_1[-1]

    def empty(self):
        if not self.stack_1:
            return True
        return False