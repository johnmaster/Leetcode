"""
执行用时 :88 ms, 在所有 python3 提交中击败了78.97%的用户
内存消耗 :14.2 MB, 在所有 python3 提交中击败了5.29%的用户

规定front和rear指针的初始位置是0
"""
class MyCircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.length = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value):
        if self.isEmpty():
            self.queue[self.front] = value
            self.rear = self.front
            return True
        else:
            temp = (self.rear + 1) % self.length
            if temp == self.front:
                return False
            self.queue[temp] = value
            self.rear = temp
            return True

    def deQueue(self):
        if not self.isEmpty():
            self.queue[self.front] = None
            if self.isEmpty():
                self.rear = self.front
                return True
            self.front = (self.front + 1) % self.length
            return True
        else:
            return False

    def Front(self):
        if not self.isEmpty():
            return self.queue[self.front]
        return -1

    def Rear(self):
        if not self.isEmpty():
            return self.queue[self.rear]
        return -1

    def isEmpty(self):
        if self.front == self.rear and self.queue[self.front] == None:
            return True
        return False

    def isFull(self):
        if self.front == (self.rear + 1) % self.length:
            return True
        return False






















