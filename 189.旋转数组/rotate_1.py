"""
三次反转
1.反转第一段，对应坐标[0, n - k - 1]
2.反转第二段，对应坐标[n - k, n - 1]
3.反转整体
执行用时 :84 ms, 在所有 python3 提交中击败了66.78%的用户
内存消耗 :15.1 MB, 在所有 python3 提交中击败了5.18%的用户
"""


class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        self.rotate_1(nums, 0, n - k - 1)
        self.rotate_1(nums, n - k, n - 1)
        self.rotate_1(nums, 0, n - 1)
        return nums

    def rotate_1(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right + 1

