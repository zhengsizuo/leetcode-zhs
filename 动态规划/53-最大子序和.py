"""最朴素的想法：遍历，O(n^2)超出时间限制"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ret = -float('INF')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sub_sum = sum(nums[i:j])
                if sub_sum > ret:
                    ret = sub_sum

        return ret

"""动态规划"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # dp数组含义：以nums[i]结尾的所有连续子数组最大和
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)

"""分治法"""