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

"""我最常用的写法"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]