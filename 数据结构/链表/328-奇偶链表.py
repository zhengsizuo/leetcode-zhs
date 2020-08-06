# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return
        if not head.next: return head

        first_head = head
        second_head = head.next
        while head:
            if not head.next or head.next.next == None:
                break
            odd_node = head.next
            head.next = head.next.next
            head = head.next

            odd_node.next = odd_node.next.next

        head.next = second_head
        return first_head