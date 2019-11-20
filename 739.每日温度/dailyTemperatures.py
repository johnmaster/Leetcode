"""
执行用时 :668 ms, 在所有 python3 提交中击败了43.14%的用户
内存消耗 :17.3 MB, 在所有 python3 提交中击败了11.63%的用户
"""
class Solution:
    def dailyTemperatures(self, T):
        output = [0] * len(T)
        stack = []
        for i, j in enumerate(T):
            while stack and T[stack[-1]] < j:
                output[stack.pop()] = i - stack[-1]
            stack.append(i)
        return output
