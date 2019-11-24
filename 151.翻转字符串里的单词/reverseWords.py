"""
执行用时 :36 ms, 在所有 python3 提交中击败了95.79%的用户
内存消耗 :14.1 MB, 在所有 python3 提交中击败了5.02%的用户
"""


class Solution:
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
