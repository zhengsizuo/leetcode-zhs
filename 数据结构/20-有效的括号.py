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

string = "()"
solution = Solution()
print(solution.isValid(string))