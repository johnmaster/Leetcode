"""
这个方法直接用深度优先搜索
结果是超时
"""
class Solution:
    def findTargetSumWays(self, nums, S):
        length = len(nums)
        return self._dfs(nums, length, 0, 0, S, [0])
    def _dfs(self, nums, length, i, sum_, S, ans):
        if i == length:
            if sum_ == S:
                ans[0] += 1
            return
        self._dfs(nums, length, i + 1, sum_ + nums[i], S, ans)
        self._dfs(nums, length, i + 1, sum_ - nums[i], S, ans)
        return ans[0]
