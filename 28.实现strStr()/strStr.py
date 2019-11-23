"""
执行用时 :92 ms, 在所有 python3 提交中击败了5.05%的用户
内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.88%的用户
"""


class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        elif not haystack:
            return -1
        length_h = len(haystack)
        length_n = len(needle)
        for i in range(length_h - length_n + 1):
            for j in range(length_n):
                if haystack[i: i + length_n] == needle
                    return i
        return i