"""
执行用时 :32 ms, 在所有 python3 提交中击败了99.27%的用户
内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.64%的用户
"""


class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1;digits[i] = digits[i] % 10
            if digits[i] != 0:
                return digits
        return [1] + digits
