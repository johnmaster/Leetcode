"""
执行用时 :428 ms, 在所有 python3 提交中击败了91.41%的用户
内存消耗 :14 MB, 在所有 python3 提交中击败了5.14%的用户
快慢指针
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        low, temp_max = 0, 0
        for quick in range(len(nums)):
            if nums[quick] == 1:
                low += 1
            else:
                temp_max = max(low, temp_max)
                low = 0
        return max(temp_max, low)