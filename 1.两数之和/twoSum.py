"""
利用哈希表完成
执行用时 :56 ms, 在所有 python3 提交中击败了96.32%的用户
内存消耗 :14.2 MB, 在所有 python3 提交中击败了43.78%的用户
"""


class Solution:
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hash:
                return [hash[temp], i]
            hash[nums[i]] = i