"""
执行用时 :36 ms, 在所有 python3 提交中击败了95.07%的用户
内存消耗 :13.7 MB, 在所有 python3 提交中击败了5.66%的用户
按照题意依次处理即可
"""


class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        answer, flag = [], 1
        pos_i, pos_j = 0, -1
        while m > 0 and n > 0:
            for i in range(n):
                pos_j += flag * 1
                answer.append(matrix[pos_i][pos_j])

            for i in range(m - 1):
                pos_i += flag * 1
                answer.append(matrix[pos_i][pos_j])
            m, n = m - 1, n - 1
            flag *= -1
        return answer