"""
执行用时 :100 ms, 在所有 python3 提交中击败了92.27%的用户
内存消耗 :15 MB, 在所有 python3 提交中击败了10.17%的用户
"""


class Solution:
    def singleNumber(self, nums):
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash.pop(i)
        return hash.popitem()[0]

