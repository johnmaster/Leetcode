"""
执行用时 :104 ms, 在所有 python3 提交中击败了79.71%的用户
内存消耗 :12.7 MB, 在所有 python3 提交中击败了99.88%的用户
"""


class Solution:
    def firstUniqChar(self, s):
        hash = {}
        for i in s:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        for i, j in hash.items():
            if j == 1:
                return s.index(i)
        return -1