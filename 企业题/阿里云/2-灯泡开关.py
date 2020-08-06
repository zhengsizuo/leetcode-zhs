"""典型动态规划"""
class Solution:
    def minFlips(self, target: str) -> int:
        dp = [0] * len(target)
        dp[0] = 0 if target[0] == '0' else 1

        for i in range(1, len(target)):
            if target[i] == target[i - 1]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + 1

        return dp[-1]