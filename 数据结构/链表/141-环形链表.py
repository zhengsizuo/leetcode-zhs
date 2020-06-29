"""双指针技巧：快慢指针"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while(fast!=None and slow!=None):
            slow = slow.next
            try:
                fast = fast.next.next
            except:
                return False
            if fast == slow:
                return True
        return False


"""哈希表法"""


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hash_set = set()
        while head:
            if head in hash_set:
                return True
            hash_set.add(head)
            head = head.next

        return False