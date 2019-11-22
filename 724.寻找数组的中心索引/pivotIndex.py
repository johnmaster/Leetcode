"""
执行用时 :256 ms, 在所有 python3 提交中击败了23.58%的用户
内存消耗 :15 MB, 在所有 python3 提交中击败了5.39%的用户
"""


class Solution:
    def pivotIndex(self, nums):
        diff, l, r = [0] * len(nums), 0, 0
        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            diff[i] += l
            l += nums[i]
            diff[j] -= r
            r += nums[j]
        return diff.index(0) if 0 in diff else -1
