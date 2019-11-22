"""
执行用时 :32 ms, 在所有 python3 提交中击败了98.34%的用户
内存消耗 :13.7 MB, 在所有 python3 提交中击败了5.26%的用户
参考  https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
遇到括号的问题一般考虑用栈解决
"""
class Solution:
    def decodeString(self, s):
        stack, res, multi = [], "", 0
        for i in s:
            if i == '[':
                stack.append((multi, res))
                multi, res = 0, ""
            elif i == ']':
                temp_multi, temp_res = stack.pop()
                res = temp_res + temp_multi * res
            elif '0' <= i <= '9':
                multi = multi * 10 + int(i)
            else:
                res += i
        return res