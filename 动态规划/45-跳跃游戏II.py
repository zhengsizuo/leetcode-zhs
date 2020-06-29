"""从后往前动态规划"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0

        dp = [float('inf') for _ in range(len(nums) - 1)]

        for i in reversed(range(len(dp))):
            if (i + nums[i]) >= len(dp):
                dp[i] = 1
            elif nums[i] == 0:
                continue
            elif nums[i] > 0:
                dp[i] = min(dp[i + 1: i + 1 + nums[i]]) + 1

        return dp[0]

"""更为高效的解法"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        maxPos = 0
        ans = 0
        for i in range(len(nums) - 1):
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                ans += 1

        return ans


nums = [2, 3, 1, 1, 4]
nums = [2]
sl = Solution()
print(sl.jump(nums))