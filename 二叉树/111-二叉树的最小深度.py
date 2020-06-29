"""BFS框架用起来"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        queue = [root]
        min_layer = 1
        while queue:
            layer_length = len(queue)  # 当前层的元素数目
            for _ in range(layer_length):
                cur = queue.pop(0)
                if not cur.left and not cur.right:
                    # 到达叶节点
                    return min_layer

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            min_layer += 1