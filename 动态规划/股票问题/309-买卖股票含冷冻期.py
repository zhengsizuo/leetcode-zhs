class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # 0表示不持有，1表示持有
        dp_i_0 = 0  # dp[i-1][0]
        dp_i_1 = -float('inf')  # dp[i-1][1]
        dp_pre_0 = 0  # dp[i-2][0]
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])  # 今天不持有，可能是昨天就不持有，或者今天卖了
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])  # 今天持有，可能是昨天就持有，或者今天买了，但是买的条件是昨天之前卖的
            dp_pre_0 = temp

        return dp_i_0