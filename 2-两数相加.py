"""提交成功"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(None)
        cur = ListNode(None)
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            var1 = 0 if l1 == None else l1.val
            var2 = 0 if l2 == None else l2.val
            carry += var1 + var2
            temp = ListNode(carry % 10)
            carry /= 10
            if ret.val == None:
                ret = temp
                cur = ret
            else:
                cur.next = temp
                cur = cur.next

            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next

        return ret