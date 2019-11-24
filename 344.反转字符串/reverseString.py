"""
执行用时 :244 ms, 在所有 python3 提交中击败了86.95%的用户
内存消耗 :17.9 MB, 在所有 python3 提交中击败了5.51%的用户
"""


class Solution:
    def reverseString(self, s):
        pre, last = 0, len(s) - 1
        while pre < last:
            temp = s[pre]
            s[pre], s[last] = s[last], temp
            pre, last = pre + 1, last - 1
        return s