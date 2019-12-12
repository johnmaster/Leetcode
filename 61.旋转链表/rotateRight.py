"""
执行用时 :36 ms, 在所有 python3 提交中击败了96.84%的用户
内存消耗 :12.5 MB, 在所有 python3 提交中击败了100.00%的用户
先将链表闭合成环
找到相应的位置断开这个环，确定新的链表头和链表尾
1.找到旧的尾部并将其与链表头连接，整个链表闭合成环，同时计算出
链表的长度n。
2.找到新的尾部，第（n - k % n - 1）个节点，新的链表头是第
（n - k % n）个节点。
"""


class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        head_1 = head
        count = 0
        while head_1.next:
            count += 1
            head_1 = head_1.next
        count += 1
        k = k % count
        if k == 0:
            return head
        head_1.next = head
        head_1 = head
        for _ in range(count - k - 1):
            head_1 = head_1.next
        new = head_1.next
        head_1.next = None
        return new