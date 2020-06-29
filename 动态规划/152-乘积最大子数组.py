"""类似53-最大子序和思路，由于负数的存在，需要维护两个数组
dp_max[i]:以i结尾的子数组乘积最大值
dp_min[i]:以i结尾的子数组乘积最小值
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp_max = [0 for _ in range(len(nums))]
        dp_min = [0 for _ in range(len(nums))]
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, len(nums)):
            dp_min[i] = min(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i])
            dp_max[i] = max(dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i], nums[i])

        return max(dp_max)