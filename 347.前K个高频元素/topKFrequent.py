"""
执行用时 :116 ms, 在所有 python3 提交中击败了92.86%的用户
内存消耗 :17.2 MB, 在所有 python3 提交中击败了7.35%的用户
"""
import collections
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        a = collections.Counter(nums)
        return heapq.nlargest(k, a.keys(), key = a.get)
