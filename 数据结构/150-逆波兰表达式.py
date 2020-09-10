class Solution:
    def evalRPN(self, tokens) -> int:
        notations = ['+', '-', '*', '/']
        stack = []

        def notation(char, item1, item2):
            if char == '+': return item1 + item2
            if char == '-': return item1 - item2
            if char == '*': return item1 * item2
            if char == '/': return int(item1 / item2)

        for t in tokens:
            # print(stack)
            if t not in notations:
                stack.append(int(t))

            else:
                first_top = stack.pop()
                second_top = stack.pop()
                new_item = notation(t, second_top, first_top)  # 次顶元素+运算符+栈顶元素
                stack.append(new_item)

        return stack[0]


"""可以用eval函数"""
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for t in tokens:
            if t in {"+", "-", "/", "*"}:
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                stack.append(str(int(eval(tmp2+t+tmp1))))
            else:
                stack.append(t)
        return int(stack.pop())


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
sl = Solution()
print(sl.evalRPN(tokens))