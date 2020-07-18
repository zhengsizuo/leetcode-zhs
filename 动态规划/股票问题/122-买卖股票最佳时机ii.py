class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0表示不持有，1表示持有
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(temp, dp_i_1 + prices[i])  # 今天不持有，可能是昨天就不持有，或者今天卖了
            dp_i_1 = max(dp_i_1, temp - prices[i])  # 今天持有，可能是昨天就持有，或者今天买了
            # print(dp_i_0, dp_i_1)

        return dp_i_0