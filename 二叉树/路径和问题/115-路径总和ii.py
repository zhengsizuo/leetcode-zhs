# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""跟112差不多，记录一下路径"""
"""如果用append函数，需要pop()重置path状态"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        res = []

        def dfs(root, sum, path):
            if not root: return
            if sum == root.val and root.left == None and root.right == None:
                path += [root.val]
                res.append(path[:])
                return

            dfs(root.left, sum - root.val, path + [root.val])
            dfs(root.right, sum - root.val, path + [root.val])

        dfs(root, sum, [])
        return res