# 二分查找，用东哥的模板
class Solution:
    def searchRange(self, nums, target):
        def left_bound(nums, target):
            left = 0
            right = len(nums) - 1

            while (left <= right):
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    # 收缩右边界
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1

            # 检查越界
            if left >= len(nums) or nums[left] != target:
                return -1
            return left

        def right_bound(nums, target):
            left = 0
            right = len(nums) - 1

            while (left <= right):
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    # 收缩左边界
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1

            # 检查越界
            if right < 0 or nums[right] != target:
                return -1
            return right

        left_bound = left_bound(nums, target)
        right_bound = right_bound(nums, target)

        return [left_bound, right_bound]