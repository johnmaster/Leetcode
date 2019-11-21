"""
图的遍历
执行用时 :44 ms, 在所有 python3 提交中击败了97.26%的用户
内存消耗 :14.4 MB, 在所有 python3 提交中击败了5.41%的用户
参考  https://leetcode-cn.com/problems/clone-graph/solution/dfs-he-bfs-by-powcai/
"""
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        visited = {}
        def dfs(node):
            if not node:
                return
            if node in visited:
                return visited[node]
            clone = Node(node.val, [])
            visited[node] = clone
            for i in node.neighbors:
                clone.neighbors.append(dfs(i))
            return clone
        return dfs(node)
