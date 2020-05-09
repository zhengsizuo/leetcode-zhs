# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
#root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
# root.right.left = TreeNode(4)
root.right.left = TreeNode(3)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or not (root.left or root.right):
            # 根节点不存在或只有一个根节点
            return True

        if root.left and root.right:
            if root.left.val != root.right.val:
                return False
        else:
            # 根节点只有一个左孩子或只有一个右孩子
            return False
        left, right = [(root.left, 'l')], [(root.right, 'r')]  # ‘l’和‘r’为标识符，标志在子树中的位置

        while (len(left) != 0 and len(right) != 0):
            r_left, left_flag = left.pop()
            r_right, right_flag = right.pop()
            # print("left element:", r_left.val, "right element:", r_right.val)
            if r_left.val != r_right.val or left_flag==right_flag:
                # 若标识符一致，说明不对称
                return False

            if r_left.left != None:
                left.append((r_left.left, 'l'))
            if r_left.right != None:
                left.append((r_left.right, 'r'))
            if r_right.right != None:
                right.append((r_right.right, 'r'))
            if r_right.left != None:
                right.append((r_right.left, 'l'))

        # 如果其中一个栈不为空，说明不对称
        if left or right:
            return False
        return True

sl = Solution()
print(sl.isSymmetric(root))

# 参考题解：https://leetcode-cn.com/problems/symmetric-tree/solution/dong-hua-yan-shi-101-dui-cheng-er-cha-shu-by-user7/