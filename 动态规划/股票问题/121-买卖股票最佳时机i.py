class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        dp = [0] * len(prices)  # 以i结尾的最大利润，即在第i天卖出股票
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i - 1])

            if prices[i] >= min_price:
                dp[i] = prices[i] - min_price

        return max(dp)

"""dp表示以i结尾的最大利润，但不一定要在第i天卖出"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_price = prices[0]
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                dp[i] = dp[i - 1]
            else:
                dp[i] = max(dp[i - 1], prices[i] - min_price)

        return dp[-1]

"""股票问题统一框架"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0表示不持有，1表示持有
        dp_i_0 = 0
        dp_i_1 = -float('inf')
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(temp, dp_i_1 + prices[i])  # 今天不持有，可能是昨天就不持有，或者今天卖了
            dp_i_1 = max(dp_i_1, - prices[i])  # 今天持有，可能是昨天就持有，或者今天买了

        return dp_i_0

prices = [7, 1, 5, 3, 6, 4]