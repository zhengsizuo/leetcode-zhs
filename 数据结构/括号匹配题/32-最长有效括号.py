"""暴力法，在20题的基础上容易想到，超出时间限制"""
brackets_dict = {')': '(', ']': '[', '}': '{'}
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # 存储括号的栈

        for c in s:
            if c in brackets_dict.keys():
                top = stack.pop() if stack else '#'  # 防止stack为空调用pop()报错
                if top != brackets_dict[c]:
                    return False
            else:
                stack.append(c)

        return not stack

    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            if s[i] in brackets_dict:
                continue

            for j in range(i + 2, len(s) + 1, 2):
                if self.isValid(s[i:j]):
                    max_len = max(max_len, len(s[i:j]))

        return max_len


"""记录括号匹配的index，转化为寻找数组最长连续序列那道128"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if stack and s[i] == ")":
                res.append(stack.pop())
                res.append(i)
            if s[i] == "(":
                stack.append(i)

        def longestConsecutive(nums):
            longest_streak = 0
            num_set = set(nums)

            for num in num_set:
                if num - 1 not in num_set:
                    current_num = num
                    current_streak = 1

                    while current_num + 1 in num_set:
                        current_num += 1
                        current_streak += 1

                    longest_streak = max(longest_streak, current_streak)

            return longest_streak

        return longestConsecutive(res)


"""用栈记录括号匹配索引，直接更新匹配长度"""

"""动态规划，难点在于(())类型的状态转移方程"""
s = "(()"