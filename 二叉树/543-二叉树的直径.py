# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_path = 0
        def maxDepth(root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if root is None:
                return 0
            else:
                left_height = maxDepth(root.left)
                right_height = maxDepth(root.right)
                self.max_path = max(self.max_path, left_height+right_height)
                return max(left_height, right_height) + 1
        maxDepth(root)
        return self.max_path