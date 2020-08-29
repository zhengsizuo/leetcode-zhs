"""奇数层反转一下列表就行"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        queue = [root]
        res = []
        level = 0
        while queue:
            res.append([])

            for _ in range(len(queue)):
                head = queue.pop(0)
                res[level].append(head.val)

                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)

            if level % 2 != 0:
                res[level].reverse()

            level += 1

        return res