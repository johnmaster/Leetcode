"""
执行用时 :52 ms, 在所有 python3 提交中击败了60.22%的用户
内存消耗 :14.4 MB, 在所有 python3 提交中击败了5.04%的用户
"""


class Solution:
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])[::-1]
