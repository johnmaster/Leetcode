"""
哈希表
执行用时 :96 ms, 在所有 python3 提交中击败了99.79%的用户
内存消耗 :12.8 MB, 在所有 python3 提交中击败了99.14%的用户
"""


from collections import defaultdict
class Solution:
    def isValidSudoku(self, board):
        row = defaultdict(set)
        col = defaultdict(set)
        block = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in row[i] and board[i][j] not in col[j] and board[i][j] not in block[(i // 3, j // 3)]:
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        block[(i // 3, j // 3)].add(board[i][j])
                    else:
                        return False
        return True