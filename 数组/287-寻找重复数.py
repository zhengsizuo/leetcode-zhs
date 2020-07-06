"""求和的方法"""
class Solution:
    def findDuplicate(self, nums) -> int:
        if not nums: return 0

        count = 0
        sum_n = sum(nums)
        for n in range(1, len(nums)):
            if n in nums:
                sum_n -= n
                count += 1

        return sum_n // (len(nums) - count)


nums = [4, 4, 4, 2, 1]

"""二分查找"""
# 遍历数组，统计小于mid的个数
"""快慢指针"""