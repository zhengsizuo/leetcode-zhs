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

"""回溯"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        num2str = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res = []

        def backtrack(digits, path):
            if not digits:
                res.append(path)
                return

            for c in num2str[digits[0]]:
                path += c
                backtrack(digits[1:], path)
                path = path[:-1]  # 字符串撤销选择

        backtrack(digits, path='')
        return res

