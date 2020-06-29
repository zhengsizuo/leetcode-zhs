"""O(nlogn)时间复杂度,O(1)空间复杂度"""
# 思路：快慢指针+归并排序
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow, fast = head, head
        while slow != None and fast != None and fast.next != None:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        head2 = slow
        pre.next = None

        return self.mergeTwoLists(self.sortList(head), self.sortList(head2))