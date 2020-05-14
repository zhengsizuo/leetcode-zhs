"""直接计数法"""
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        memo = {0: 0, 1: 0, 2: 0}
        for n in nums:
            memo[n] += 1
        print(memo)

        nums[:memo[0]] = [0]*memo[0]
        nums[memo[0]:memo[0]+memo[1]] = [1]*memo[1]
        nums[memo[0]+memo[1]:] = [2]*memo[2]


nums = [2,0,2,1,1,0]
sl = Solution()
sl.sortColors(nums)
print(nums)

"""三指针，快速排序"""