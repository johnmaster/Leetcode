"""
利用哈希表完成
执行用时 :104 ms, 在所有 python3 提交中击败了95.65%的用户
内存消耗 :20.3 MB, 在所有 python3 提交中击败了73.73%的用户
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        hash = {}
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = i
            else:
                if abs(i - hash[nums[i]]) <= k:
                    return True
                else:
                    hash[nums[i]] = i
        return False
