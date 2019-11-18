"""
广度优先搜索
执行用时 :688 ms, 在所有 python3 提交中击败了40.09%的用户
内存消耗 :14.9 MB, 在所有 python3 提交中击败了10.21%的用户
"""
class Solution:
    def numSquares(self, n):
        if n == 0:
            return 0
        visited = set()
        queue = [(n, 0)]
        step = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                temp, step = queue.pop(0)
                for j in range(1, int(temp ** 0.5) + 1):
                    temp_1 = temp - j ** 2
                    if temp_1 == 0:
                        return step + 1
                    if temp_1 not in visited:
                        visited.add(temp_1)
                        queue.append((temp_1, step + 1))
        return step