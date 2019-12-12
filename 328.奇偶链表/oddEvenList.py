"""
执行用时 :40 ms, 在所有 python3 提交中击败了98.73%的用户
内存消耗 :14.4 MB, 在所有 python3 提交中击败了99.47%的用户

利用两个指针，第一个指针odd指向奇数位节点，第二个指针even指向
偶数位节点。
在循环开始之前，应用一个变量记录偶数位开始的地方，不可在循环结束
后将odd的next指向head.next，因为这时的head.next已经指向了第二
个奇数位。
在遍历过程中，由于even在odd后面，所以当even为空指针时，odd已经
将所有的奇数位节点全部找到，应结束循环。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        if not head:
            return head
        odd = head
        even = head.next
        temp = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = temp
        return head