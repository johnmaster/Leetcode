"""
广度优先搜索
执行用时 :624 ms, 在所有 python3 提交中击败了86.03%的用户
内存消耗 :14.9 MB, 在所有 python3 提交中击败了8.33%的用户
"""
class Solution:
    def openLock(self, deadends, target):
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        queue = [('0000', 0)]
        while queue:
            temp, step = queue.pop(0)
            for i in range(4):
                for j in [-1, 1]:
                    temp_1 = temp[:i] + str((int(temp[i]) + j) % 10) + temp[i+1:]
                    if temp_1 == target:
                        return step + 1
                    if temp_1 not in deadends:
                        deadends.add(temp_1)
                        queue.append((temp_1, step + 1))
        return -1