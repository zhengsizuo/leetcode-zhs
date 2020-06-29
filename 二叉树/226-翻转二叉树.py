# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 上递归模板就完事了
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        if root.left == None and root.right == None:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left

        return root