"""
动态规划在字符串问题中的常见做法：定义dp[i][j]表示s的前i个字符与p的前j个字符是否匹配
难点在于根据模式串p中*的不同情况写状态转移方程
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = ' ' + s
        p = ' ' + p
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n)] for _ in range(m)]
        dp[0][0] = True
        # 初始化第一行
        for j in range(1, n):
            if p[j] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m):
            for j in range(1, n):
                if p[j] != '*':
                    if p[j] == '.' or p[j]==s[i]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False

                else:
                    if p[j-1] == s[i] or p[j-1] == '.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]  # 匹配多次或者不匹配
                    else:
                        dp[i][j] = dp[i][j-2]  # 不匹配

        # print(dp)
        return dp[-1][-1]
s = 'aab'
p = 'c*a*b'
sl = Solution()
print(sl.isMatch(s, p))
