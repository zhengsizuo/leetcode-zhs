"""动态规划， 斐波拉契数列"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 动态规划
        dp = [0, 1, 2]
        if n < 3:
            return dp[n]

        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[n]