"""
一个高度平衡的二叉搜索树（平衡二叉搜索树）是在插入和删除任何节点之后
可以自动保持其高度最小。也就是说，有N个节点的平衡二叉搜索树，它的高
度是logN。并且，每个节点的两个子树的高度不会相差超过1。
根据定义，我们可以判断一个二叉搜索树是否是高度平衡的（平衡二叉树）。
正入我们之前提到的，一个有N个节点的平衡二叉搜索树的高度总是LogN。
因此，我们可以计算节点总数和树的高度，以确定这个二叉搜索树是否是高
度平衡的。
同样，在定义中，我们提到了高度平衡的二叉树一个特性：每个节点的两个子
树的深度不会相差超过1。我们也可以根据这个性质，递归的验证树。

为什么需要用到高度平衡的二叉搜索树？
当分析二叉搜索树的相关操作时，我们需要注意的是树的高度是十分重要的，
如果树的高度为h，则时间复杂度为O(h)，二叉搜索树的高度的确很重要。
所以，我们来讨论一下树的节点总数N和高度h之间的关系。对于一个平衡二叉树
前文提过，h>logN。但对一个普通的二叉搜索树，在最坏的情况下，它可以退化
为一个链。
因此，具有N个节点的二叉搜索树的高度在logN和N区间变化，也就是说，搜索
操作的时间复杂度可以从logN变化到N。这是一个巨大的性能差异。
所以说，高度平衡的二叉搜索树对提高性能起着重要作用。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        return self.dfs(root) != -1

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        if left == -1: return -1
        right = self.dfs(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(right - left) < 2 else -1
