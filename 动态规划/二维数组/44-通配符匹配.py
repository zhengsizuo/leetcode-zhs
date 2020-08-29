"""与10-正则表达式类似，状态转移方程还更简单一些"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = ' ' + s
        p = ' ' + p
        m, n = len(s), len(p)
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for j in range(1, n):
            if p[j] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                if p[j] == s[i] or p[j] == '?':
                    dp[i][j] = dp[i - 1][j - 1]

                if p[j] == '*':
                    # 使用*号和不使用*号
                    dp[i][j] = dp[i][j - 1] or dp[i-1][j]  # dp[i][j-1]表示不匹配

        # for d in dp:
        #     print(d)
        return dp[-1][-1]


s = 'acdcb'
p = 'a*c?b'
sl = Solution()
print(sl.isMatch(s, p))