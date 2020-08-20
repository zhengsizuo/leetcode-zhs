class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        zero_cnt = nums.count(0)
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                continue
            elif nums[i+1] == nums[i]:
                return False
            elif nums[i + 1] - nums[i] != 1:
                zero_cnt -= (nums[i + 1] - nums[i] - 1)
                # print(zero_cnt)
                if zero_cnt < 0:
                    return False

        return True

"""可以不排序解决此题, max-min < 5"""
nums = [0, 0, 1, 2, 6]
sl = Solution()
print(sl.isStraight(nums))