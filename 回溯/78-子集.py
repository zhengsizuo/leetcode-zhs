class Solution:
    def subsets(self, nums):
        if not nums:
            return []

        result = [[]]

        def backtrack(path, nums):
            # print(nums)
            # 递归终止条件
            if len(nums) == 0:
                return

            for i in range(len(nums)):
                path.append(nums[i])  # 做选择
                result.append(path[:])
                backtrack(path, nums[i+1:])  # nums[i+1:]表示从选择列表的其他选项搜索
                path.remove(nums[i])  # 移除选择

        backtrack([], nums)
        return result

nums = [1, 2, 3]
sl = Solution()
print(sl.subsets(nums))
