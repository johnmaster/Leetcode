class Solution(object):
    def findPeakElement(self, nums):
        size = len(nums)
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left