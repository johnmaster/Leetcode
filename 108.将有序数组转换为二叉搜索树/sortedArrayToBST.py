"""
执行用时 :72 ms, 在所有 python3 提交中击败了98.90%的用户
内存消耗 :14.9 MB, 在所有 python3 提交中击败了100.00%的用户

题目说明是升序数组，则二叉搜索树的中序遍历刚好是一个升序数组，所以
题目给出的升序数组就是二叉搜索树的中序遍历。

平衡二叉搜索树需要保证两点
1.根节点大于左子树任意节点，小于右子树任意节点。
2.左右子树高度相差不超过1
由以上性质，一个可行的递归条件可以得出：
1.每次返回的根节点处于数组中间，以其左右半数组分别递归构造左右子树
2.那么就意味着左子树小于根节点，右子树大于根节点，且所有节点左右子树
节点数相差不超过1（由于递归的构树方式相同，所有节点都满足高度平衡）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        target = len(nums) // 2
        root = TreeNode(nums[target])
        root.left = self.sortedArrayToBST(nums[:target])
        root.right = self.sortedArrayToBST(nums[target + 1:])
        return root