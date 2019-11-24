"""
执行用时 :48 ms, 在所有 python3 提交中击败了46.25%的用户
内存消耗 :13.6 MB, 在所有 python3 提交中击败了5.56%的用户

j 行的数据，应该由j - 1行的数据计算出来
假设 j - 1行为[1, 3, 3, 1], 那么我们在前面插入一个0(j行的数据会比j - 1行多一个)
然后执行相加[0 + 1, 1 + 3, 3 + 3, 3 + 1, 1] = [1, 4, 6, 4, 1],最后一个1保留即可
"""


class Solution:
    def getRow(self, rowIndex):
        original = [1]
        for i in range(1, rowIndex + 1):
            original = [0] + original
            for j in range(i):
                original[j] = original[j] + original[j + 1]
        return original
        