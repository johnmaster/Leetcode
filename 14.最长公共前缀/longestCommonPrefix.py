"""
执行用时 :48 ms, 在所有 python3 提交中击败了65.56%的用户
内存消耗 :13.7 MB, 在所有 python3 提交中击败了5.53%的用户
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        index = 1
        first_word = strs[0]
        while index < len(strs):
            while strs[index].find(first_word) != 0:
                first_word = first_word[:len(first_word) - 1]
            index += 1
        return first_word