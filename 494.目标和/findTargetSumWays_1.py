"""
动态规划方法
执行用时 :1316 ms, 在所有 python3 提交中击败了7.68%的用户
内存消耗 :19.4 MB, 在所有 python3 提交中击败了5.88%的用户
"""
class Solution:
    def findTargetSumWays(self, nums, S):
        length, dp = len(nums), {(0, 0) : 1}
        for i in range(1, length + 1):
            for j in range(-sum(nums), sum(nums) + 1):
                dp[(i, j)] = dp.get((i - 1, j - nums[i - 1]), 0) + dp.get((i - 1, j + nums[i + 1]), 0)
        return dp.get((length, S), 0)


