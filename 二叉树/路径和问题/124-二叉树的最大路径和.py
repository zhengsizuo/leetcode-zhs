# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxSum = -float('inf')

    def maxPathSum(self, root) -> int:
        def maxGain(root):
            if not root:
                return 0

            left_gain = max(maxGain(root.left), 0)
            right_gain = max(maxGain(root.right), 0)

            prePathsum = root.val + left_gain + right_gain
            self.maxSum = max(prePathsum, self.maxSum)
            node_gain = root.val + max(left_gain, right_gain)
            return node_gain

        maxGain(root)
        return self.maxSum