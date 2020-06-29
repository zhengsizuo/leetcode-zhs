class Solution:
    def largestSquareArea(self, heights) -> int:
        stack = [-1]
        area = 0
        heights.append(0)
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                edge = min(h, (i-stack[-1]-1))  # 选最小的边组成正方形
                area = max(area, edge**2)
            stack.append(i)
        heights.pop()

        return area

    def maximalSquare(self, matrix) -> int:
        if not matrix: return 0
        max_area = 0
        dp = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[j] += 1
                else:
                    dp[j] = 0

            max_area = max(max_area, self.largestSquareArea(dp))

        return max_area

"""直接动态规划"""
# dp(i,j) 表示以(i,j)为右下角，且只包含1的正方形的边长最大值
# dp[i, j] = min(dp[i-1,j], dp[i-1, j-1], dp[i, j-1])+1
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

sl = Solution()
print(sl.maximalSquare(matrix))