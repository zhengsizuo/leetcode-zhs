# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 走完一趟之后A跑到B, B跑到A，消除长度差
# 并没有改变链表结构
# 就算不相交，最终也会共同指向NULL
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha