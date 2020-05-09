# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(7)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(100)

"""带备忘录的自顶向下递归"""
class Solution:
    memo = dict()

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 备忘录消除重叠子问题
        if root in self.memo.keys():
            return self.memo[root]
        ret = 0
        money = root.val
        if root.left:
            money += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            money += self.rob(root.right.left) + self.rob(root.right.right)

        # money是抢之后去下下家（孙子); 与不抢，去下家（儿子）比较大小
        ret = max(money, self.rob(root.left) + self.rob(root.right))
        self.memo[root] = ret
        return ret

sl = Solution()
ret = sl.rob(root)
print(ret)