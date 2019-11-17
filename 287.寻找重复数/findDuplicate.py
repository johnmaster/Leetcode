"""
二分法
执行用时 :64 ms, 在所有 python 提交中击败了77.83%的用户
内存消耗 :13.6 MB, 在所有 python 提交中击败了29.62%的用户
"""
class Solution(object):
    def findDuplicate(self, nums):
        size = len(nums)
        left = 1
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for target in nums:
                if target <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left 