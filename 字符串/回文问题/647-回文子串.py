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
