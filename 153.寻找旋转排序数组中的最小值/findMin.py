#寻找旋转位置就是最小的值
class Solution(object):
    def findMin(self, nums):
        size = len(nums)
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]