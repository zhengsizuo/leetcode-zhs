# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leaf_path = dict()
        self.path = []
        def dfs(root):
            if not root:
                return
            self.path.append(root.val)
            if not root.left and not root.right:
                leaf_path[root.val] = self.path[::-1]
                self.path = []
                return

            dfs(root.left)
            if root.val not in self.path:
                self.path.append(root.val)
            dfs(root.right)

        dfs(root)
        print(leaf_path)
        count = 0
        for leaf1, path1 in leaf_path.items():
            for leaf2, path2 in leaf_path.items():
                if leaf1 == leaf2: continue
                for i in range(len(path1)):
                    if path1[i] in path2:
                        d = i + path2.index(path1[i])
                        if d <= distance:
                            count += 1

        return count // 2



class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root or not root.left and not root.right:
            return 0

        def _dfs(root):
            """获取左右子树中叶子结点到当前节点的距离"""
            if not root:
                return {}
            # 叶子节点
            if not root.left and not root.right:
                return {root: 0}

            left_leaf = _dfs(root.left)
            right_leaf = _dfs(root.right)
            # 距离加1
            for k, v in left_leaf.items(): left_leaf[k] = v + 1
            for k, v in right_leaf.items(): right_leaf[k] = v + 1
            print(left_leaf, right_leaf)

            for lk, lv in left_leaf.items():
                for rk, rv in right_leaf.items():
                    if lv + rv <= distance:
                        self.ans += 1

            # 合并左右子树的叶子节点，向上返回
            left_leaf.update(right_leaf)
            return left_leaf

        self.ans = 0
        _dfs(root)
        return self.ans


# 作者：dz - lee
# 链接：https: // leetcode - cn.com / problems / number - of - good - leaf - nodes - pairs / solution / dfsshen - du - yi - ci - bian - li - python3 - by - dz - lee /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

sl = Solution()
print(sl.countPairs(root, 4))