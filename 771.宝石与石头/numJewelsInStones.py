"""
执行用时 :32 ms, 在所有 python3 提交中击败了92.86%的用户
内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.52%的用户
"""


class Solution:
    def numJewelsInStones(self, J, S):
        stone = set(J)
        return sum(i in stone for i in s)
    