# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""思路：先序遍历，所有节点是上一节点的右孩子"""
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        prev_root = root
        while(stack):
            tail = stack.pop()
            if tail.right:
                stack.append(tail.right)
            if tail.left:
                stack.append(tail.left)
            if tail != root:
                prev_root.right = tail  # 上一个节点的右孩子指向当前节点
                prev_root.left = None  # 并且置左孩子为none
                prev_root = tail