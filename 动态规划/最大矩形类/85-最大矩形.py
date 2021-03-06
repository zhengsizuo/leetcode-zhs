"""利用84的解法，求出每层的heights数组"""

class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = [-1]
        area = 0
        heights.append(0)
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                area = max(area, h * (i - stack[-1] - 1))
            stack.append(i)
        heights.pop()

        return area

    def maximalRectangle(self, matrix) -> int:
        if not matrix: return 0

        res = 0
        dp = [0] * len(matrix[0])  # 从matrix中构建heights数组
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[j] += 1
                else:
                    dp[j] = 0
            res = max(res, self.largestRectangleArea(dp))

        return res


""""更普适的动态规划法"""


class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix: return 0

        res = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # 同行前面（包括自身）有多少个1，前缀和

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                else:
                    dp[i][j] = dp[i][j - 1] + 1 if j > 0 else 1
                    w = float('inf')
                    for k in range(i, -1, -1):
                        # 回溯前面的行
                        h = i - k + 1
                        w = min(w, dp[k][j])
                        res = max(res, w * h)
                        print("k: %d \t j:%d \t w: %d \t " % (k, j, w))
                        if w == 0:
                            break

        return res

matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

sl = Solution()
print(sl.maximalRectangle(matrix))



