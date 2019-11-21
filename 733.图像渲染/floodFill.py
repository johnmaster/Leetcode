"""
广度优先搜索
执行用时 :164 ms, 在所有 python3 提交中击败了16.86%的用户
内存消耗 :13.5 MB, 在所有 python3 提交中击败了6.02%的用户
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        originalC = image[sr][sc]
        queue = [(sr, sc)]
        while queue:
            pos_i, pos_j = queue.pop(0)
            image[pos_i][pos_j] = newColor
            for direction in directions:
                new_i = pos_i + direction[0]
                new_j = pos_j + direction[1]
                if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == originalC:
                    queue.append((new_i, new_j))
                    image[new_i][new_j] = newColor
        return image
