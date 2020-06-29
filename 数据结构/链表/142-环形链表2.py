# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            # 相遇，结束循环
            if slow == fast:
                slow = head
                while (slow != fast):
                    slow = slow.next
                    fast = fast.next

                return slow

        return None