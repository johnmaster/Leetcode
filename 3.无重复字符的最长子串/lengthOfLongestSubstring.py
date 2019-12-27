"""
执行用时 :64 ms, 在所有 python3 提交中击败了88.03%的用户
内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.63%的用户
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        hash, ans = {}, 0
        j = 0
        for i in range(len(s)):
            if s[i] in hash:
                j = max(hash[s[i]], j)
            ans = max(i - j + 1, ans)
            hash[s[i]] = i + 1
        return ans