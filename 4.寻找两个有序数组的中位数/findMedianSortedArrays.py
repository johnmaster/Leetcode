"""
二分法
执行用时 :124 ms, 在所有 python3 提交中击败了75.14%的用户
内存消耗 :14.1 MB, 在所有 python3 提交中击败了5.28%的用户
参考 https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (self.recursion(nums1, 0, m- 1, nums2, start2, end2, left) + self.recursion(nums1, start1, end1, nums2, start2, end2, right))

    def recursion(self, nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2:
            return self.recursion(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            return nums2[start2 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])

        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1

        if nums1[i] > nums2[j]:
            return self.recursion(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.recursion(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))

