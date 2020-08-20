"""dp[i][j]：字符从i到j位置回文子序列的最大长度，倒着遍历"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # 初始化对角线
        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # print(dp)
        return dp[0][-1]


s = 'bbbab'
sl = Solution()
print(sl.longestPalindromeSubseq(s))