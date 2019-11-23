"""
执行用时 :40 ms, 在所有 python3 提交中击败了83.47%的用户
内存消耗 :13.8 MB, 在所有 python3 提交中击败了5.59%的用户
"""


class Solution:
    def generate(self, numRows):
        dp = [[0] * n for n in range(1, numRows + 1)]
        for i in range(numRows):
            dp[i][0] = dp[i][-1] = 1
        for i in range(numRows):
            for j in range(i + 1):
                if dp[i][j] == 0:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp