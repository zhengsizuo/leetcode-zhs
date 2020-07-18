class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        stack = []  #存储括号的栈
        brackets_dict = {'(':')', '[':']','{':'}'}
        for item in s:
            if len(stack) != 0:
                if stack[-1] in brackets_dict.keys():
                    if brackets_dict[stack[-1]] == item:
                        stack.pop()
                    else:
                        stack.append(item)
                else:
                    stack.append(item)
            else:
                stack.append(item)
        
        return not stack

"""更简洁的写法"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  #存储括号的栈
        brackets_dict = {')':'(', ']':'[','}':'{'}

        for c in s:
            if c in brackets_dict.keys():
                top = stack.pop() if stack else '#'  # 防止stack为空调用pop()报错
                if top != brackets_dict[c]:
                    return False

            else:
                stack.append(c)

        return not stack


string = "()[]{}"
solution = Solution()
print(solution.isValid(string))