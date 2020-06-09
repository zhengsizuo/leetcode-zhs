# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        path = {p: [], q: []}

        def DFS(root, layer, target):
            if not root:
                return

            layer += 1
            path[target].append((root.val, layer))
            if root == target:
                return

            DFS(root.left, layer, target)
            DFS(root.right, layer, target)

        DFS(root, 0, p)
        DFS(root, 0, q)
        print(path[p])
        print(path[q])

        if len(path[p]) > len(path[q]):
            path[p], path[q] = path[q], path[p]

        for i in reversed(range(len(path[p]))):
            if path[p][i] in path[q]:
                return path[p][i]


"""简洁题解"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root


# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/


p = root.left
q = root.right

sl = Solution()
print(sl.lowestCommonAncestor(root, p, q))