"""
执行用时 :36 ms, 在所有 python3 提交中击败了98.41%的用户
内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.37%的用户
"""


class Solution:
    def removeElement(self, nums, val):
        low = 0
        for quick in range(len(nums)):
            if nums[quick] != val:
                nums[low] = nums[quick]
                low += 1
        return low