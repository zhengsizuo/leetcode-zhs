# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def create_list(list):
    """
    :param list: list[int]
    :return: ListNode
    """
    listnodes = []
    for i in range(len(list)):
        listnodes.append(ListNode(list[i]))

    for i in range(len(listnodes)-1):
        listnodes[i].next = listnodes[i+1]

    return listnodes[0], listnodes


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        # 以头指针较小的节点作为新链表的的head
        if l1.val <= l2.val:
            head = l1
        else:
            head = l2
            l2 = l1
            l1 = head


        while (True):
            if l1.next == None:
                l1.next = l2
                break
            if l2 == None:
                break
            while l1.val <= l2.val < l1.next.val:
                tmp = l2.next
                l2.next = l1.next
                l1.next = l2
                l2 = tmp

                if l2 == None:
                    break
            l1 = l1.next
            print(l1.val)

        return head

"""递归解法"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2  # 终止条件，直到两个链表都空
        if not l2: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2



l1_list = [-10, -10, -9, -4, 1, 6, 6]
l2_list = [-7]

l1, L1 = create_list(l1_list)
l2, L2 = create_list(l2_list)
print(L1)

sl = Solution()
head = sl.mergeTwoLists(l1, l2)

while head != None:
    print(head.val)
    head = head.next