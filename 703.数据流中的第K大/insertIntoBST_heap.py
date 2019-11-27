"""
大顶堆小顶堆
堆是一种非线性结构，可以把堆看成一个数组，也可以被看成一个完全
二叉树，通俗来讲堆其实就是利用完全二叉树的结构来维护的一维数组
按照堆的特点可以把堆分成大顶堆和小顶堆
大顶堆：每个结点的值都大于或等于其左右孩子结点的值
小顶堆：每个结点的值都小于或等于其左右孩子结点的值
堆和普通树的区别：
内存占用：普通树占用的内存比它们存储的数据要多，堆仅仅使用数组
且不使用指针。
平衡：
二叉搜索树必须是"平衡"的情况下，其大部分操作的复杂度才能达到
O(nlog2n)
搜索：
在二叉树中搜索会很快，但是在堆中搜索会很慢。在堆中搜索不是第一
优先级，因为使用堆的目的是将最大（或者最小）的结点放在前面，从
而快速的进行相关插入，删除操作。
堆排序的过程
将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的
根节点，将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余
n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。
如此反复执行，就能得到一个有序序列了，建立最大堆时是从最后一个
非叶子结点开始从下往上调整。


执行用时 :164 ms, 在所有 python3 提交中击败了39.03%的用户
内存消耗 :17.5 MB, 在所有 python3 提交中击败了5.63%的用户
"""

import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        print(self.nums)
        return self.nums[0]

