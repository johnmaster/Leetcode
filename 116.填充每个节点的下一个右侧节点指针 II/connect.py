#广度优先搜索
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: "Node"):
        if not root:
            return
        queue = [root]
        while queue:
            pre = None
            for _ in range(len(queue)):
                temp = queue.pop(0)
                if pre:
                    pre.next = temp
                pre = temp
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return root