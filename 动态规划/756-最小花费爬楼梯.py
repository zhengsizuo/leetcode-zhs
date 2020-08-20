class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[-1], dp[-2])


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
cost = [10, 15, 20]
sl = Solution()
print(sl.minCostClimbingStairs(cost))