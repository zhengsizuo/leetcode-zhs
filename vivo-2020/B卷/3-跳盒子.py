'''
 Welcome to vivo ! LeetCode-45 原题
'''


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

step_list = [int(i) for i in input().split()]
step_list = [2, 3, 1, 1, 4]
print(solution(step_list))