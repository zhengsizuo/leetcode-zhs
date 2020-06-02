"""暴力回溯法，超出时间限制"""
class Solution:
    directs = [(0, 1), (1, 0)]

    def uniquePaths(self, m: int, n: int) -> int:
        num_paths = []

        def backtrack(i, j):
            if i == n - 1 and j == m - 1:
                num_paths.append(1)
                return
            for direct in self.directs:
                cur_i = i + direct[0]
                cur_j = j + direct[1]
                if cur_i < n and cur_j < m:
                    backtrack(cur_i, cur_j)

        backtrack(0, 0)
        return sum(num_paths)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i+1 == n and j+1 < m:
                    # 最后一行往右边更新
                    dp[i][j] = dp[i][j + 1]
                if j+1 == m and i+1 < n:
                    # 最后一列向下更新
                    dp[i][j] = dp[i+1][j]
                elif i+1 < n and j+1 < m:
                    # 其他情况综合往右和往下的情况
                    dp[i][j] = dp[i][j + 1] + dp[i+1][j]

        return dp[0][0]


sl = Solution()
print(sl.uniquePaths(3, 2))