"""
执行用时 :32 ms, 在所有 python3 提交中击败了98.13%的用户
内存消耗 :12.6 MB, 在所有 python3 提交中击败了99.59%的用户

一次遍历算法
上述算法可以优化为只使用一次遍历，我们可以使用两个指针而不是一个
指针，第一个指针从列表的开头向前移动n + 1步，而第二个指针将从列
表的开头出发。现在，这两个指针被n个结点分开。我们通过同时移动两
个指针向前来保持这个恒定的间隔，直到第一个指针到达最后一个结点，
此时第二个指针将指向从最后一个结点数起的第n个结点。我们重新链接
第二个指针所引用的结点的next指针指向该结点的下下个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        block = ListNode(None)
        block.next = head
        start = block
        end = block
        i = 0

        while i < n + 1:
            end = end.next
            i += 1

        while end:
            start = start.next
            end = end.next

        start.next = start.next.next
        block = block.next
        return block 