"""二维数组的动态规划解法
dp[i][j]表示数组前i个元素，组成和为j的方案数
"""
class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        if not nums:
            return 0



"""带记忆优化的DFS，自顶向下的动态规划"""
from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        @lru_cache(None)
        def dp(i, cur_sum):
            # 数组前i个元素和为cur_sum的方案数
            print("dp(i, j): ", i, cur_sum)
            if i == 0: return 0
            if i == 1 and (cur_sum == nums[0] and cur_sum == -nums[0]):
                # 当数组首位为0时，+/-都可以，故返回两种
                return 2
            if i == 1 and (cur_sum == nums[0] or cur_sum == -nums[0]):
                return 1
            if cur_sum > sum(nums[:i]) or cur_sum < -sum(nums[:i]):
                return 0

            return dp(i - 1, cur_sum - nums[i - 1]) + dp(i - 1, cur_sum + nums[i - 1])

        return dp(len(nums), S)


nums = [1, 1, 1, 1, 1]
S = 3
nums = [0,0,0,0,0,0,0,0,1]
S = 1

sl = Solution()
print(sl.findTargetSumWays(nums, S))