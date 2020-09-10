# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)


def search(root, nodes):
    if root == None:
        return
    nodes.append(root.val)
    search(root.left, nodes)
    search(root.right, nodes)

nodes = []
search(root, nodes)
print(nodes)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        # 用堆栈遍历二叉树, (根节点, 下界, 上界)的元组形式储存
        nodes = []
        nodes.append((root, float('-inf'), float('inf')))

        while (len(nodes) != 0):
            cur_root, lower, upper = nodes.pop()
            val = cur_root.val
            if val <= lower or val >= upper:
                return False

            if cur_root.right != None:
                nodes.append((cur_root.right, val, upper))
            if cur_root.left != None:
                nodes.append((cur_root.left, lower, val))

        return True

# sl = Solution()
# print(sl.isValidBST(root))


"""官方题解"""
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
