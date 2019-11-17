"""
二分法
******* 这道题十分典型 **********
执行用时 :84 ms, 在所有 python 提交中击败了94.12%的用户
内存消耗 :12.2 MB, 在所有 python 提交中击败了40.00%的用户
"""
class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums = sorted(nums)
        left = 0
        right = max(nums) - min(nums)
        while left < right:
            mid = left + (right - left) // 2
            j, count = 0, 0
            for i in range(1, len(nums)):
                while nums[i] - nums[j] > mid:
                    j += 1
                count += i - j
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left