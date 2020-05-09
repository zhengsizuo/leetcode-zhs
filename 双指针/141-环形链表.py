# 双指针技巧：快慢指针或使用哈希表
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