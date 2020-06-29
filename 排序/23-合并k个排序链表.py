# Definition for singly-linked list.
class ListNode:
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

    return listnodes[0]

class Solution:
    def mergeKLists(self, lists):

        for l in lists[:]:
            # 移除[]项
            if not l:
                lists.remove(l)

        if not lists:
            return None

        # 递归终止条件
        if len(lists) == 1:
            return lists[0]

        k = 0
        min_l = lists[0]
        for i in range(1, len(lists)):
            if lists[i].val < min_l.val:
                min_l = lists[i]
                k = i

        if min_l.next != None:
            lists[k] = min_l.next
        else:
            lists.remove(min_l)

        min_l.next = self.mergeKLists(lists)
        return min_l

"""分治法"""
"""优先级队列"""
l1_list = [1, 4, 5]
l2_list = [1, 3, 4]
l3_list = [2, 6]

lists = [create_list(l1_list), create_list(l2_list), create_list(l3_list)]
sl = Solution()
head = sl.mergeKLists(lists)

while head != None:
    print(head.val)
    head = head.next