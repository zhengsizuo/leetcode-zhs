"""回溯，暴力递归"""
class Solution:
    def threeSum(self, nums):
        if not nums:
            return []

        result = []
        def backtrack(path, nums):
            if len(path) == 3:
                path.sort()
                if sum(path) == 0 and path not in result:
                    result.append(path[:])

                return

            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(path, nums[:i]+nums[i+1:])
                path.remove(nums[i])

        backtrack([], nums)

        return result

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


nums = [-1, 0, 1, 2, -1, -4]
sl = Solution()
print(sl.threeSum(nums))
