"""
二分法
执行用时 :40 ms, 在所有 python 提交中击败了69.40%的用户
内存消耗 :11.8 MB, 在所有 python 提交中击败了37.63%的用户
"""
class Solution(object):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    nums2 = sorted(nums2)
    inter_set = []
    size = len(nums2)
    for target in nums1:
        left = 0
        right = size - 1
        while left < right:
            while left < right and nums2[left] == nums2[left + 1]:
                left += 1
            while left < right and nums2[right] == nums2[right - 1]:
                right -= 1
            mid = left + (right - left) // 2
            if nums2[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left == right and nums2[left] == target and target not in inter_set:
            inter_set.append(target)
    return inter_set