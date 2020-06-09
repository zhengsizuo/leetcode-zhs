"""二维数组的动态规划解法
dp[i][j]表示数组前i个元素，组成和为j的方案数
"""
class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        if not nums:
            return 0



"""带记忆优化的DFS"""
nums = [1, 1, 1, 1, 1]
S = 3
sl = Solution()
print(sl.findTargetSumWays(nums, S))