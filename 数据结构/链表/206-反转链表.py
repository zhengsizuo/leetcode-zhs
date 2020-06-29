# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归法，搞清楚递归函数的输入输出即可
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return last

# 迭代法，设置前置指针prev
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp

        return prev

