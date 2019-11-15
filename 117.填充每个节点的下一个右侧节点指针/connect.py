class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root:Node):
        if not root:
            return
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp.left:
                temp.left.next = temp.right
                if temp.next:
                    temp.right.next = temp.next.left
                stack.append(temp.right)
                stack.append(temp.left)
        return root