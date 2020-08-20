"""双指针"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                break

        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            else:
                j += 1