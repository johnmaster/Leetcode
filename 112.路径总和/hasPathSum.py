class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def hasPathSum(self, root:TreeNode, sum:int):
        if not root:
            return False
        stack = [(root, sum - root.val)]
        while stack:
            root, temp = stack.pop()
            if root.left == None and root.right == None and temp == 0:
                return True
            if root.left:
                stack.append((root.left, temp - root.left.val))
            if root.right:
                stack.append((root.right, temp - root.right.val))
        return False
