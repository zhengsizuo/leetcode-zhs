class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        delta = len(nums) - k + 1
        if delta <= 0:
            return []

        dp = [0] * delta
        dp[0] = max(nums[:k])
        for i in range(1, delta):
            if nums[i - 1] == dp[i - 1]:
                dp[i] = max(nums[i:i + k])
            elif nums[i + k - 1] > dp[i - 1]:
                dp[i] = nums[i + k - 1]
            elif nums[i + k - 1] <= dp[i - 1]:
                dp[i] = dp[i - 1]

        return dp

"""双向队列"""