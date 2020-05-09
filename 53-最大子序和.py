"""最朴素的想法：遍历，超出时间限制"""

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