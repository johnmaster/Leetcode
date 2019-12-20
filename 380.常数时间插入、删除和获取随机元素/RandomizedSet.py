"""
利用哈希表和列表
执行用时 :600 ms, 在所有 python3 提交中击败了6.09%的用户
内存消耗 :16.8 MB, 在所有 python3 提交中击败了77.66%的用户
"""


import random


class RandomizedSet:
    def __init__(self):
        self.hash = {}
        self.values = []

    def insert(self, val):
        if val not in self.values:
            self.hash[val] = len(self.values)
            self.values.append(val)
            return True
        else:
            return False

    def remove(self, val):
        if val in self.values:
            self.hash[self.values[-1]] = self.hash[val]
            self.values[self.hash.pop(val)] = self.values[-1]
            self.values.pop()
            return True
        else:
            return False

    def getRandom(self):
        return self.values[random.randint(0, len(self.values) - 1)]
