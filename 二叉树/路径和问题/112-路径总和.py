"""官方题解"""
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

"""自己写的，与官方题解思路一致"""
class Solution:
    def hasPathSum(self, root, sum: int) -> bool:
        if not root: return False
        if sum == root.val and root.left==None and root.right==None:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""深度优先，到第106个测试用例有问题"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if root.val == sum:
            if root.left==None and root.right==None:
                return True
            if root.left or root.right:
                return False

        def dfs(root, cur_sum):
            if not root:
                if cur_sum==sum:
                    return True
                else:
                    return False
            cur_sum += root.val
            return dfs(root.left, cur_sum) or dfs(root.right, cur_sum)

        return dfs(root, 0)