"""迭代遍历，超出时间限制"""
class Solution:
    def dailyTemperatures(self, T):
        if not T: return []

        delta = []
        for i in range(len(T) - 1):
            delta.append(T[i] - T[i + 1])

        res = [0] * len(T)
        for i in range(len(delta)):
            if delta[i] < 0:
                res[i] = 1
            else:
                for j in range(i + 1, len(delta)):
                    delta[i] += delta[j]
                    if delta[i] < 0:
                        res[i] = j - i + 1
                        break

                if delta[i] > 0:
                    # 如果仍然大于0，说明之后都不会升高
                    res[i] = 0

        return res


"""单调栈解法"""

class Solution:
    def dailyTemperatures(self, T):
        if not T: return []

        res = [0] * len(T)
        stack = [0]
        for i in range(1, len(T)):
            while T[i] > T[stack[-1]]:
                cur_i = stack.pop()
                res[cur_i] = i - cur_i  # 升高的天数
                if not stack:
                    break

            stack.append(i)

        return res


T = [73, 74, 75, 71, 69, 72, 76, 73]
sl = Solution()
print(sl.dailyTemperatures(T))