# 使用辅助栈
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack)==0 or x <= self.minStack[-1]:
            # 相等的情况也需要压入栈
            self.minStack.append(x)

    def pop(self) -> None:
        top_element = self.stack.pop()
        if top_element == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]