"""二维数组动态规划"""
# dp[i][j]：word1的前i个字符变换到word2的前j个字符所需的最少操作数
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = ' ' + word1
        word2 = ' ' + word2
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 初始化第一行第一列
        for i in range(n):
            dp[0][i] = i
        for j in range(m):
            dp[j][0] = j

        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]  # 什么都不用做

                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1  # 对应删、增、改

        return dp[-1][-1]
