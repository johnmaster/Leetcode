"""
二分查找
执行用时 :36 ms, 在所有 python 提交中击败了89.72%的用户
内存消耗 :11.7 MB, 在所有 python 提交中击败了32.98%的用户
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        # nums1始终表示最小的那一个
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        inter_set = []
        nums2 = sorted(nums2)
        for target in nums1:
            left = self.left_bound(nums2, target)
            if left != -1:
                inter_set.append(target)
                nums2.pop(left)
        return inter_set

    def left_bound(self, nums2, target):
        size = len(nums2)
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums2[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums2[left] == target:
            return left
        else:
            return -1