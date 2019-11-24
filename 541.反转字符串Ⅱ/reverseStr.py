"""
执行用时 :40 ms, 在所有 python3 提交中击败了89.76%的用户
内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.84%的用户
"""


class Solution:
    def reversStr(self, s, k):
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return "".join(s)
