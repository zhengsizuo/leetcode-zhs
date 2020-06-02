"""暴力递归"""
# class Solution:
#     directs = [(0, 1), (1, 0)]  # 只能右或下
#
#     def minPathSum(self, grid):
#         m = len(grid)
#         n = len(grid[0])
#         result = []
#         path = 0
#
#         def search(grid, i, j, path):
#             path += (grid[i][j])
#             if i == (m-1) and j == (n-1):
#                 result.append(path)
#                 return
#             for direct in self.directs:
#                 cur_i = i + direct[0]
#                 cur_j = j + direct[1]
#                 if cur_i >= 0 and cur_i < m and cur_j >= 0 and cur_j < n:
#                     search(grid, cur_i, cur_j, path)
#
#         search(grid, 0, 0, path)
#
#         return min(result)


"""动态规划，m*n二维数组"""


class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = grid[m - 1][n - 1]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 == m and j+1<n:
                    # 最后一行往右边更新
                    dp[i][j] = dp[i][j + 1] + grid[i][j]
                if j + 1 == n and i+1<m:
                    # 最后一列往下更新
                    dp[i][j] = dp[i+1][j] + grid[i][j]
                elif i+1<m and j+1<n:
                    # 其他情况比较往右和往下的情况
                    dp[i][j] = min(dp[i][j + 1] + grid[i][j], dp[i+1][j] + grid[i][j])

        return dp[0][0]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
sl = Solution()
print(sl.minPathSum(grid))