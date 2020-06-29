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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        cur_pos = 1
        head_first = head
        node_pre = None
        while head != None:
            if cur_pos == (m - 1):
                node_pre = head

            if cur_pos == m:
                node_m = head
                prev = None
                curr = node_m
                while curr != None:
                    if cur_pos == (n+1):
                        break
                    # 迭代反转链表的m到n位置，需要记住m-1的位置和n+1的位置
                    next_tmp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_tmp
                    cur_pos += 1

                node_m.next = curr  # 连接尾部
                if node_pre:
                    node_pre.next = prev  # 连接头部
                    return head_first
                else:
                    # 若m=1，则直接返回prev节点
                    return prev

            head = head.next
            cur_pos += 1


"""递归法"""

l1_list = [3, 5]
l1, _ = create_list(l1_list)

sl = Solution()
new_head = sl.reverseBetween(l1, 1, 2)
while new_head:
    print(new_head.val)
    new_head = new_head.next