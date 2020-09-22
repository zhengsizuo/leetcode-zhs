"""超时108/109"""
class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        s = s.replace(" ", "")
        operator = ['+', '-', '*', '/']
        # 运算符栈和数字栈分开放
        num_stack = []
        operator_stack = []

        j = 0
        num_str = ''
        while j < len(s):
            if s[j] in operator:
                num_stack.append(int(num_str))
                num_str = ''
                operator_stack.append(s[j])
            else:
                num_str += s[j]
            j += 1

        if len(num_str)!=0:
            num_stack.append(int(num_str))

        i = 0
        while i < len(operator_stack):
            # print(operator_stack)
            op = operator_stack[i]
            if op in operator[2:]:
                a = num_stack[i]
                b = num_stack[i + 1]
                if op == '*':
                    c = a * b
                elif op == '/':
                    c = int(a / b)

                num_stack.insert(i, c)
                num_stack.remove(a)
                num_stack.remove(b)
                operator_stack.remove(op)
                # print(operator_stack, num_stack)

            else:
                i += 1

        while operator_stack:
            op = operator_stack.pop(0)
            a = num_stack.pop(0)
            b = num_stack.pop(0)
            if op == '+':
                c = a + b
            elif op == '-':
                c = a - b
            num_stack.insert(0, c)

        return num_stack[0]


"""参考题解"""
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0; sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if s[i] in '+-*/' or i == len(s)-1:
                # print(stack, sign, num)
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0; sign = s[i]
        return sum(stack)

#
# 作者：elevenxx
# 链接：https://leetcode-cn.com/problems/basic-calculator-ii/solution/zhan-by-elevenxx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
s = "3+2*2"
s = '42+2*3/2 - 1'
sl = Solution()
print(sl.calculate(s))