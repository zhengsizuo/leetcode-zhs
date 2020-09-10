# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
k = 1

# 先LDR中序遍历，再二分查找数组位置或者直接输出第k-1个元素
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root: return 0

        ldr_list = []

        def search(root):
            if not root: return
            search(root.left)
            ldr_list.append(root.val)
            search(root.right)

        search(root)

        # return ldr_list[k-1]
        #print(ldr_list)
        left = 0
        right = len(ldr_list)

        mid = (left + right) // 2
        #print(mid)
        k = k-1
        while k != mid:
            if k < mid:
                right = mid
            if k > mid:
                left = mid
            mid = (left + right) // 2

        return ldr_list[mid]


"""官方题解，迭代"""
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


# 作者：LeetCode
# 链接：https: // leetcode - cn.com / problems / kth - smallest - element - in -a - bst / solution / er - cha - sou - suo - shu - zhong - di - kxiao - de - yuan - su - by - le /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

sl = Solution()
print(sl.kthSmallest(root, 1))