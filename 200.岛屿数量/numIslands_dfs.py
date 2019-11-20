"""
深度优先搜索
执行用时 :160 ms, 在所有 python3 提交中击败了89.95%的用户
内存消耗 :15 MB, 在所有 python3 提交中击败了14.55%的用户
"""
class Solution:
    def __init__(self):
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def numIslands(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and grid[i][j] == '1':
                    count += 1
                    self._dfs(grid, i, j, m, n, visited)
        return count

    def _dfs(self, grid, i, j, m, n, visited):
        visited[i][j] = True
        for direction in self.directions:
            cur_i = i + direction[0]
            cur_j = j + direction[1]
            if 0 <= cur_i < m and 0 <= cur_j < n and visited[cur_i][cur_j] == False and grid[cur_i][cur_j] == '1':
                self._dfs(grid, cur_i, cur_j, m, n, visited)

