"""
二分法
********** 很经典的方法 ***********
执行用时 :12 ms, 在所有 python 提交中击败了100.00%的用户
内存消耗 :11.8 MB, 在所有 python 提交中击败了53.13%的用户
"""
class Solution(object):
    def splitArray(self, nums, m):
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            temp, count = 0, 1
            for i in nums:
                temp += i
                if temp > mid:
                    count += 1
                    temp = i
            if count > m:
                left = mid + 1
            else:
                right = mid
        return left