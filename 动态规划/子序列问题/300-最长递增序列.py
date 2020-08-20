class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        # 以nums[i]结尾的最长递增子序列长度
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                # 往前遍历，找到比当前数小的才更新dp数组
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


nums = [10,9,2,5,3,7,101,18]
sl = Solution()
print(sl.lengthOfLIS(nums))