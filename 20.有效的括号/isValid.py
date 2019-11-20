"""
执行用时 :32 ms, 在所有 python3 提交中击败了99.12%的用户
内存消耗 :14 MB, 在所有 python3 提交中击败了5.51%的用户
"""
class Solution:
    def isValid(self, s):
        if not s:
            return True
        stack = []
        for i in s:
            if i == '(' or i =='{' or i == '[':
                stack.append(i)
            else:
                if stack == []:
                    return False
                else:
                    temp = stack.pop() + i
                    if temp not in ['[]', '{}', '()']:
                        return False
        if stack == []:
            return True
        else:
            return False
