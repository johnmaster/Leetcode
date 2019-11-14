#递归法
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetric(self, root:TreeNode):
        if not root:
            return True
        return self.is_symmetric(root.left, root.right)
    def is_symmetric(self, root_left, root_right):
        if root_left == None and root_right == None:
            return True
        if root_left == None and root_right != None or root_left != None and root_right == None:
            return False
        return (root_left.val == root_right.val) and self.is_symmetric(root_left.left, root_right.right) and self.is_symmetric(root_left.right, root_right.left)