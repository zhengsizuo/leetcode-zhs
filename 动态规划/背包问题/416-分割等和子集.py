"""类似贪心思想，到第100个测试用例失效"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        sum_n = sum(nums)
        half_sum = sum_n // 2
        if sum_n % 2 != 0:
            return False
        else:
            cur_sum = 0
            i = 0
            while i!=len(nums):
                cur_sum += nums[i]
                if cur_sum == half_sum:
                    return True
                if cur_sum > half_sum:
                    cur_sum -= nums[i]

                i += 1

            return False

"""0-1背包动态规划，套背包框架"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_n = sum(nums)
        half_sum = sum_n // 2
        if sum_n % 2 != 0:
            return False

        dp = [[False for _ in range(half_sum + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            # 容量为0时即认为可以装满
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, half_sum + 1):
                if (j - nums[i - 1]) < 0:
                    # 不装入
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 可以选择装入或不装入
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]


nums = [11, 5, 5, 2, 1]