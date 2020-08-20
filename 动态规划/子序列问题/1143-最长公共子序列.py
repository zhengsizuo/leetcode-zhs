class Solution:
    def longestCommonSubsequence(self, text1, text2) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        # 初始化第一行第一列
        for j in range(1, n):
            dp[0][j] = 1 if text1[0] == text2[j] else dp[0][j - 1]
        for i in range(1, m):
            dp[i][0] = 1 if text1[i] == text2[0] else dp[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i] != text2[j]:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i-1][j-1] + 1  # LCS增加一个字符

        for d in dp:
            print(d)
        return dp[-1][-1]


text1 = "bsbm"
text2 = "mbk"
sl = Solution()
print(sl.longestCommonSubsequence(text1, text2))


# 1035-不相交的直线，代码一模一样：https://leetcode-cn.com/problems/uncrossed-lines/description/