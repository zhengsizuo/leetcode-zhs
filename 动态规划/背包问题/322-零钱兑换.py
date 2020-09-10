"""自顶向下，备忘录"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()

        def dp(amount):
            if amount in memo.keys():
                return memo[amount]
            if amount < 0:
                return -1
            if amount == 0:
                return 0

            res = float('INF')
            for coin in coins:
                sub_problem = dp(amount - coin)
                if sub_problem == -1:
                    # 子问题无解，跳过
                    continue
                res = min(res, dp(amount - coin) + 1)

            memo[amount] = res if res != float('INF') else -1
            return res if res != float('INF') else -1

        return dp(amount)


"""自底向上，状态转移方程不变"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != float('inf') else -1