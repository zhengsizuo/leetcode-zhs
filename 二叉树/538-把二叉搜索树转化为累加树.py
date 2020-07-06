# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(5)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(13)
root.right.left = TreeNode(8)
root.right.right = TreeNode(20)

"""先深度优先递归用栈保存，LDR中序遍历"""
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return

        stack = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            stack.append(root)
            dfs(root.right)

        dfs(root)
        pre_sum = stack.pop().val
        while stack:
            cur_node = stack.pop()
            cur_node.val += pre_sum
            pre_sum = cur_node.val

        return root

"""官方题解，递归"""
class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree/solution/ba-er-cha-sou-suo-shu-zhuan-huan-wei-lei-jia-shu-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
sl = Solution()
sl.convertBST(root)
