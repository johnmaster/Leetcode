"""
执行用时 :288 ms, 在所有 python3 提交中击败了88.55%的用户
内存消耗 :33.7 MB, 在所有 python3 提交中击败了100.00%的用户
"""


class Solution:
    def fourSumCount(self, A, B, C, D):
        hash, ans = {}, 0
        for i in A:
            for j in B:
                if i + j not in hash:
                    hash[i + j] = 1
                else:
                    hash[i + j] += 1
        for i in C:
            for j in D:
                if -(i + j) in hash:
                    ans += hash[-(i + j)]
        return ans