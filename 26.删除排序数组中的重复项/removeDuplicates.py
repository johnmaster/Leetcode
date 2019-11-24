"""
执行用时 :108 ms, 在所有 python3 提交中击败了79.28%的用户
内存消耗 :15.4 MB, 在所有 python3 提交中击败了5.25%的用户
"""


class Solution:
    def removeDuplicates(self, nums):
        low = 0
        for quick in range(1, len(nums)):
            if nums[quick] != nums[low]:
                low += 1
                if low != quick:
                    nums[quick], nums[low] = nums[low], nums[quick]
        return low + 1