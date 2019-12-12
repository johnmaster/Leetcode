"""
执行用时 :28 ms, 在所有 python3 提交中击败了99.85%的用户
内存消耗 :13.8 MB, 在所有 python3 提交中击败了99.62%的用户

双指针迭代
申请两个指针，第一个指针叫pre,最初指向None。
第二个指针叫cur，最初指向head,然后不断遍历cur。
每次迭代到cur，都将cur的next指向pre,然后pre和cur前进一位
都迭代完了（cur变成None），pre就是最后一个节点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre