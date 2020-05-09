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

"""核心思路：让队列只维持当前层的元素"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [root]
        ret = []
        layer = 0  # 维护所在层数
        while queue:
            ret.append([])
            layer_length = len(queue)  # 当前层的元素数目
            for i in range(layer_length):
                cur_root = queue.pop(0)
                ret[layer].append(cur_root.val)
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)

            layer += 1

        return ret

sl = Solution()
ret = sl.levelOrder(root)
print(ret)