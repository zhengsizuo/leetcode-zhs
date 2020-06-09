class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1

        if target >= nums[0]:
            # 从头往后找
            for i in range(len(nums)):
                if target == nums[i]:
                    return i
                if nums[i] < nums[0] or i == len(nums) - 1:
                    # 如果到突变的位置还没找到，返回-1
                    return -1

        else:
            # 从后往前找
            if target > nums[-1]:
                return -1
            for i in reversed(range(len(nums))):
                if target == nums[i]:
                    return i
                if nums[i] > nums[-1] or i == 0:
                    return -1


"""官方题解，二分搜索"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]