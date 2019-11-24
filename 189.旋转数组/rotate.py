"""
超出时间限制
但是方法是对的
"""


class Solution:
    def rotate(self, nums, k):
        length = len(nums)
        for i in range(k):
            temp_last = nums[length - 1]
            for j in range(length):
                temp = nums[j]
                nums[j] = temp_last
                temp_last = temp
        return nums