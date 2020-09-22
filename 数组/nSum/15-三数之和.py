"""双指针法，时间复杂度O(n^2)"""
class Solution:
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []

        nums.sort()  # 先对数组排序
        res = []

        for k in range(len(nums) - 2):
            # 直接跳过的两种情况
            if nums[k] > 0:
                continue
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            left = k + 1
            right = len(nums) - 1
            while left < right:
                if nums[k] + nums[left] + nums[right] == 0:
                    res.append([nums[k], nums[left], nums[right]])
                    # 去除重复
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1

                elif nums[k] + nums[left] + nums[right] < 0:
                    # while left<right and nums[left]==nums[left+1]: left += 1
                    left += 1
                elif nums[k] + nums[left] + nums[right] > 0:
                    # while left<right and nums[right]==nums[right-1]: right -= 1
                    right -= 1

        return res


"""把twoSum函数往上加"""
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3: return []

        def twoSum(nums, target: int):
            if not nums: return []

            nums.sort()
            l = 0
            r = len(nums) - 1
            res = []
            while l < r:
                left, right = nums[l], nums[r]
                sum_ = left + right
                if sum_ < target:
                    while l < r and nums[l] == left:
                        l += 1
                elif sum_ > target:
                    while l < r and nums[r] == right:
                        r -= 1
                elif sum_ == target:
                    res.append([left, right])
                    while l < r and nums[l] == left:
                        l += 1
                    while l < r and nums[r] == right:
                        r -= 1

            return res

        ret = []
        nums.sort()
        # print(nums)
        for k in range(len(nums) - 2):
            if k > 0 and nums[k-1] == nums[k]:
                continue
            two_list = twoSum(nums[k + 1:], -nums[k])
            if two_list:
                for l in two_list:
                    ret.append([nums[k]] + l)

        return ret


nums = [-1, 0, 1, 2, -1, -4]
sl = Solution()
print(sl.threeSum(nums))
