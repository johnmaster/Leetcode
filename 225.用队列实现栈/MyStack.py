"""
用双队列实现栈
执行用时 :44 ms, 在所有 python3 提交中击败了61.13%的用户
内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.88%的用户
"""


class MyStack:
    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []

    def push(self, x):
        if not self.queue_1:
            self.queue_1.append(x)
        else:
            while self.queue_1:
                self.queue_2.append(self.queue_1.pop(0))
            self.queue_1.append(x)
            while self.queue_2:
                self.queue_1.append(self.queue_2.pop(0))
        return True

    def pop(self):
        if self.queue_1:
            return self.queue_1.pop(0)
        return False

    def top(self):
        if self.queue_1:
            return self.queue_1[0]

    def empty(self):
        if not self.queue_1:
            return True
        return False