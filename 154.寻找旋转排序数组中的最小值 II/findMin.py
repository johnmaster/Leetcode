"""
执行用时 :44 ms, 在所有 python 提交中击败了83.70%的用户
内存消耗 :12 MB, 在所有 python 提交中击败了27.00%的用户
"""
class Solution(object):
    def findMin(self, nums):
        size = len(nums)
        left = 0
        right = size - 1
        while left < right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
