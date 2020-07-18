"""带备忘录的回溯，通过"""
from functools import lru_cache
class Solution:
    def removeInvalidParentheses(self, s: str):
        if len(s)==0:
            return [""]

        def isValid(s):
            # 判断字符串是否为有效的括号组合
            stack = []
            for c in s:
                if c not in ['(', ')']:
                    continue
                if c == '(':
                    stack.append(c)
                if c == ')':
                    top = stack[-1] if stack else '#'
                    if top == '(':
                        stack.pop()
                    else:
                        stack.append(c)

            return not stack

        def Counter(s):
            # 统计字符串s中不匹配的左右括号数
            stack = []
            left, right = 0, 0
            for c in s:
                if c not in ['(', ')']:
                    continue
                if c == '(':
                    stack.append(c)
                if c == ')':
                    top = stack[-1] if stack else '#'
                    if top == '(':
                        stack.pop()
                    else:
                        right += 1
            left = len(stack)
            return left, right

        left, right = Counter(s)
        # print(left, right)
        result = set()

        @lru_cache(None)
        def backtrack(s, left_c=0, right_c=0):
            if left_c == left and right_c == right:
                result.add(s)

            for i in range(len(s)):
                if s[i] not in ['(', ')']:
                    continue
                if s[i] == '(' and left_c < left:
                    left_c += 1
                    backtrack(s[:i] + s[i + 1:], left_c, right_c)
                    left_c -= 1
                if s[i] == ')' and right_c < right:
                    right_c += 1
                    backtrack(s[:i] + s[i + 1:], left_c, right_c)
                    right_c -= 1

        backtrack(s)
        # print(result)
        ret = []
        for s in result:
            if isValid(s):
                ret.append(s)

        return ret


s ='()))((()'
s = "(a)())()"
s = '()())()'
sl = Solution()

print(sl.removeInvalidParentheses(s))