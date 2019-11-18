"""
广度优先搜索
执行用时 :192 ms, 在所有 python3 提交中击败了60.87%的用户
内存消耗 :14.8 MB, 在所有 python3 提交中击败了14.55%的用户
"""
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == False:
                    visited[i][j] = True
                    count += 1
                    queue = [(i, j)]
                    while queue:
                        pos_i, pos_j = queue.pop(0)
                        for direction in directions:
                            cur_i = pos_i + direction[0]
                            cur_j = pos_j + direction[1]
                            if 0 <= cur_i< m and 0 <= cur_j < n and visited[cur_i][cur_j] == False and grid[cur_i][cur_j] == '1':
                                visited[cur_i][cur_j] = True
                                queue.append((cur_j, cur_j))
        return count
