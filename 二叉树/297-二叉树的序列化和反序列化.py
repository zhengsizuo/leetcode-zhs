import json
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)

root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        pre_order = []
        in_order = []

        def pre_search(root):
            if not root:
                # ret.append(None)
                return
            pre_order.append(root.val)
            pre_search(root.left)
            pre_search(root.right)

        def in_search(root):
            if not root:
                # ret.append(None)
                return
            in_search(root.left)
            in_order.append(root.val)
            in_search(root.right)

        pre_search(root)
        in_search(root)
        pre_str = str(pre_order).replace(' ', '')
        in_str = str(in_order).replace(' ', '')

        return pre_str + '+' + in_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        plus_idx = data.index('+')
        pre_str, in_str = data[:plus_idx][1:-1], data[plus_idx + 1:][1:-1]
        pre_order = [int(pre) for pre in pre_str.split(',')]
        in_order = [int(pre) for pre in in_str.split(',')]

        def build_tree(pre_order, in_order):
            if len(pre_order) == 0 or len(in_order) == 0:
                return

            root = TreeNode(pre_order[0])
            mid_idx = in_order.index(pre_order[0])
            root.left = build_tree(pre_order[1:mid_idx + 1], in_order[:mid_idx])
            root.right = build_tree(pre_order[mid_idx + 1:], in_order[mid_idx + 1:])
            return root

        return build_tree(pre_order, in_order)


"""用层序遍历完成，序列化和反序列化时都使用queue来维护"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'

        queue = [root]
        res = []
        while queue:
            root = queue.pop(0)
            if root:
                res.append(str(root.val))
                queue.append(root.left)
                queue.append(root.right)
            else:
                res.append('#')

        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return

        i = 1
        vals = data[1:-1].split(',')
        print(vals)
        root = TreeNode(int(vals[0]))
        queue = [root]

        while queue:
            node = queue.pop(0)
            if vals[i] != '#':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != '#':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1

        return root


"""深度优先，DLR先序遍历"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(root):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        # print(vals)
        vals = iter(vals)  # 把列表转换为迭代器
        def dfs():
            v = next(vals)
            if v == '#': return

            node = TreeNode(int(v))
            node.left = dfs()
            node.right = dfs()
            return node

        root = dfs()
        return root



codec = Codec()
data = codec.serialize(root)
print(data)
print(codec.deserialize(data))
