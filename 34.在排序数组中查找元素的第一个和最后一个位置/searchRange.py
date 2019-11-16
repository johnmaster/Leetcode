class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        left = self.left_search(nums, target)
        right = self.right_search(nums, target)
        return [left, right]
    def left_search(self, nums, target):
        #左中位数
        size = len(nums)
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            return left
        else:
            return -1
    def right_search(self, nums, target):
        #右中位数
        size = len(nums)
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[left] == target:
            return left
        return -1