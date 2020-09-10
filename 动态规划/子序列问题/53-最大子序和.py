
"""动态规划"""
class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0

        # dp数组含义：以nums[i]结尾的所有连续子数组最大和
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]

"""分治法"""