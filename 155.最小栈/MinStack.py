"""
执行用时 :740 ms, 在所有 python3 提交中击败了19.75%的用户
内存消耗 :17.4 MB, 在所有 python3 提交中击败了5.08%的用户
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.index = -1
    def push(self, x):
        self.stack.append(x)
        self.index += 1
    def pop(self):
        self.stack.pop()
        self.index -= 1
    def top(self):
        return self.stack[self.index]
    def getMin(self):
        return min(self.stack)

