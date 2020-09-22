# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""迭代法"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseK(head, k):
            cnt = 0
            tmp = head
            while cnt < k and tmp:
                tmp = tmp.next
                cnt += 1
            if cnt == k:
                # 若剩下长度大于等于k，需要翻转
                cnt = 0
                prev = None
                curr = head
                while cnt < k and curr:
                    next_tmp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_tmp
                    cnt += 1

                return head, prev, curr

            else:
                # 不需要翻转，直接返回原链表
                return None, head, None

        head, prev, curr = reverseK(head, k)  # 原始头部，新的头部，下一个待翻转头部
        # k个一组翻转链表，改变结构
        while head:
            new_head, new_prev, curr = reverseK(curr, k)
            head.next = new_prev
            head = new_head

        return prev