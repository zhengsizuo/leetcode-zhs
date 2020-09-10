"""暴力回溯，超时"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        if not coins: return 0

        result = []

        def backtrack(cur_amount, path):
            if cur_amount == 0:
                path.sort()
                if path not in result:
                    result.append(path[:])
                return
            for c in coins:
                cur_amount -= c
                path.append(c)
                if cur_amount >= 0:
                    backtrack(cur_amount, path)
                path.remove(c)
                cur_amount += c

        backtrack(amount, [])
        return len(result)


"""完全背包问题"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][amount]