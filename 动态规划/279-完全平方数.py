# 几乎等于零钱兑换模板，只需求出可以用的零钱coins数组即可
class Solution:
    def numSquares(self, n: int) -> int:
        import math
        x = math.sqrt(n)
        coins = []
        for i in range(1, int(x)+1):
            coins.append(i**2)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[n] if dp[n] != float('inf') else -1