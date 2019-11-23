"""
执行用时 :40 ms, 在所有 python3 提交中击败了84.29%的用户
内存消耗 :13.7 MB, 在所有 python3 提交中击败了5.56%的用户
"""


class Solution:
    def getRow(self, rowIndex):
        rowIndex += 1
        dp = [[0] * n in range(1, rowIndex + 1)]
        for i in range(rowIndex):
            dp[i][0] = dp[i][-1] = 1
        for i in range(rowIndex):
            for j in range(i + 1):
                if dp[i][j] == 0:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp[-1]
