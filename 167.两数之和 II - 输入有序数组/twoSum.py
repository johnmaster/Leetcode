"""
二分法
执行用时 :52 ms, 在所有 python 提交中击败了87.63%的用户
内存消耗 :12 MB, 在所有 python 提交中击败了25.21%的用户
"""
class Solution(object):
    def twoSum(self, numbers, target):
        size = len(numbers)
        left = 0
        right = size - 1
        while left < right:
            temp = numbers[left] + numbers[right]
            if temp > target:
                right -= 1
            elif temp < target:
                left += 1
            else:
                return [left + 1, right + 1]
