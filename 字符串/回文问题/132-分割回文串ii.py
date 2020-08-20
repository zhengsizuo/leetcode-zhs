"""直接在131回溯法上面改，超时"""
class Solution:
    def minCut(self, s: str) -> int:
        def is_valid(s):
            return s == s[::-1]

        res = float('inf')
        def backtrack(s, path):
            nonlocal res
            if not s:
                if len(path) < res:
                    res = len(path)
                return

            for j in range(len(s)):
                if is_valid(s[:j+1]):
                    backtrack(s[j+1:], path + [s[:j+1]])

        backtrack(s, [])

        return res - 1


"""动态规划，dp[i]表示前缀串s[:i]分割成若干个回文子串所需要最小分割次数"""
# dp[i] = min(dp[j]+1 for j in range(i) if s[j+1:i]是回文串)