"""
执行用时 :40 ms, 在所有 python3 提交中击败了94.40%的用户
内存消耗 :12.6 MB, 在所有 python3 提交中击败了99.67%的用户
"""


class Solution:
    def isIsomorphic(self, s, t):
        hash = {}
        for c1, c2 in zip(s, t):
            if c1 in hash and hash[c1] != c2:
                return False
            if c1 not in hash and c2 in hash.values():
                return False
            hash[c1] = c2
        return True