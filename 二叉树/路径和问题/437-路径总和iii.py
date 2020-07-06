# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.right = TreeNode(-3)
# root.right.left = TreeNode(5)
root.right.right = TreeNode(11)

"""121 / 126 个通过测试用例"""
import functools
class Solution:
    def __init__(self):
        self.count = 0

    def pathSum(self, root, sum: int) -> int:
        @functools.lru_cache()
        def dfs(root, cur_sum):
            if not root:
                return
            cur_sum += root.val
            # print(cur_sum)
            if cur_sum == sum:
                self.count += 1
                # return
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)

        queue = [root]
        while queue:
            root = queue.pop(0)
            dfs(root, cur_sum=0)
            if root.left:
               queue.append(root.left)
            if root.right:
                queue.append(root.right)

        return self.count


"""一个简洁的题解，不需要双重递归"""


class Solution:
    def pathSum(self, root, sum: int) -> int:
        if not root: return 0

        def dfs(root, sum_list):
            if not root: return 0
            sum_list = [num + root.val for num in sum_list] + [root.val]
            return sum_list.count(sum) + dfs(root.left, sum_list) + dfs(root.right, sum_list)

        return dfs(root, [])

sl = Solution()
print("res:", sl.pathSum(root, sum=8))
