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

    return listnodes[0], listnodes

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True

        fore_list, before_list = [], []
        slow, fast = head, head

        while slow!=None and fast!=None and fast.next!=None:

            fore_list.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        while slow!=None:
            before_list.append(slow.val)
            slow = slow.next

        # 处理链表长度为奇数的情况
        if len(fore_list) < len(before_list):
            before_list.pop(0)
        print(fore_list, before_list)
        if fore_list == before_list[::-1]:
            return True
        else:
            return False


"""快慢指针加反转链表"""
"""反转链表可以用迭代和递归两种方法"""



l1_list = [1, 0, 1]
l1, _ = create_list(l1_list)
head = l1
# while head != None:
#     print(head.val)
#     head = head.next

sl = Solution()
print(sl.isPalindrome(l1))
