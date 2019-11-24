"""
执行用时 :364 ms, 在所有 python3 提交中击败了81.81%的用户
内存消耗 :16.4 MB, 在所有 python3 提交中击败了5.23%的用户
"""


class Solution:
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        sum_num = 0
        for i in range(0, len(nums), 2):
            sum_num += nums[i]
        return sum_num
