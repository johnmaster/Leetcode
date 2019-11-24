"""
滑动窗口双指针
执行用时 :80 ms, 在所有 python3 提交中击败了100.00%的用户
内存消耗 :16.7 MB, 在所有 python3 提交中击败了5.14%的用户
"""


class Solution:
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        res = float('inf')
        left, temp = 0, 0
        for right in range(n):
            temp += nums[left]
            while temp >= s:
                res = min(res, right - left + 1)
                temp -= nums[left]
                left += 1
        return res if res != float('inf') else 0
