"""提交成功版本：队列法"""

# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         if len(digits) == 0:
#             return []
#
#         num_to_str = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
#                       ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
#
#         ret = ['']
#         for d in digits:
#             for _ in range(len(ret)):
#                 temp = ret.pop(0)
#                 for letter in num_to_str[int(d) - 2]:
#                     ret.append(temp + letter)
#
#         return ret

""""""
# 考虑用树的遍历怎么做
class TreeNode(object):
    def __init__(self, x):
        self.data = x
        self.children = None


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        num_to_str = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                      ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        digits_int = []
        for d in digits:
            digits_int.append(int(d) - 2)

        # for str_list in digits_str:
        #     for i, item in enumerate(str_list):
        #         str_list[i] = TreeNode(item)
        #
        # for i in range(len(digits_str)-1):
        #     for tree_node in digits_str[i]:
        #         tree_node.children = digits_str[i+1]

