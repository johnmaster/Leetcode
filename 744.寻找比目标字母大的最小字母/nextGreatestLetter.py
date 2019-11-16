#二分查找
"""
执行用时 :88 ms, 在所有 python 提交中击败了90.50%的用户
内存消耗 :13.8 MB, 在所有 python 提交中击败了7.89%的用户
"""
class Solution(obejct):
    def nextGreatestLetter(self, letters, target):
        size = len(letters)
        left = 0
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2
            if ord(letters[mid]) <= ord(target):
                left = mid + 1
            else:
                right = mid
        if letters[left] == target or ord(letters[left]) < ord(target):
            return letters[0]
        return letters[left]
