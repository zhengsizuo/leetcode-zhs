"""中心双指针扩展法"""
class Solution:
    def expand(self, s, l, r, count):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1
        return count

    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            count = self.expand(s, i, i, count)
            count = self.expand(s, i, i + 1, count)

        return count


"""动态规划法, dp表"""
# 若s[i..j]为回文串，则dp[i][j]=True
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        # 初始化base case，对角线即单个字符的时候为True
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)-1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i == 1:
                        # 特殊情况
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

        res = 0
        for dp_i in dp:
            res += dp_i.count(True)

        return res


s = 'acaaa'
sl = Solution()
print(sl.countSubstrings(s))