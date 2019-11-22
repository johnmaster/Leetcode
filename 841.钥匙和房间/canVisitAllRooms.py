"""
执行用时 :104 ms, 在所有 python3 提交中击败了49.31%的用户
内存消耗 :14.3 MB, 在所有 python3 提交中击败了5.63%的用户
"""


class Solution:
    def canVisitAllRooms(self, rooms):
        visited, queue = {0}, [0]
        while queue:
            temp = queue.pop()
            for i in rooms[temp]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return len(rooms) == len(visited)
