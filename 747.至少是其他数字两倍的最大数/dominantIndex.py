"""
贪心算法
执行用时 :64 ms, 在所有 python3 提交中击败了26.57%的用户
内存消耗 :13.7 MB, 在所有 python3 提交中击败了5.53%的用户
参考 https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/solution/onde-ji-su-ti-jie-python3-c-by-jimmy00745/
"""
class Solution:
    def dominantIndex(self, nums):
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        max_index = 0
        flag = True
        for i in range(1, len(nums)):
            if nums[i] > nums[max_index]:
                flag = nums[i] >= nums[max_index] * 2
                max_index = i
            else:
                if flag:        #这个flag处理的非常好
                   flag = nums[max_index] >= nums[i] * 2
        if not flag:
            return -1
        else:
            return max_index
