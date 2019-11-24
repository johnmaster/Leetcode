"""
执行用时 :64 ms, 在所有 python3 提交中击败了84.15%的用户
内存消耗 :15 MB, 在所有 python3 提交中击败了6.26%的用户
"""


class Solution:
    def moveZeroes(self, nums):
        low = 0
        for quick in range(len(nums)):
            if nums[quick] != 0:
                nums[quick], nums[low] = nums[low], nums[quick]
            low += 1
        return nums