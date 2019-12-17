"""
执行用时 :140 ms, 在所有 python3 提交中击败了96.31%的用户
内存消耗 :18.2 MB, 在所有 python3 提交中击败了85.18%的用户
"""


class Solution:
    def containsDuplicate(self, nums):
        hash = set()
        for i in nums:
            if i not in hash:
                hash.add(i)
            else:
                return True
        return False