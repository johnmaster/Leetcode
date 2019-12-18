"""
执行用时 :36 ms, 在所有 python3 提交中击败了94.62%的用户
内存消耗 :12.5 MB, 在所有 python3 提交中击败了99.43%的用户
"""


class Solution:
    def isHappy(self, n):
        n = str(n)
        visited = set()
        while 1:
            n = str(sum(int(i) ** 2 for i in n))
            if n == '1':
                return True
            if n in visited:
                return False
            visited.add(n)