class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        result = []
        def backtrack(path, nums):
            if len(path) == len(nums):
                # print('path:', path)
                result.append(path[:])  # 注意一定做一次拷贝，或path.copy()，因为Python是引用赋值
                return

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path, nums)
                path.remove(num)

        backtrack([], nums)
        return result

# class Solution:
#     def permute(self, nums):
#         res = []
#         def backtrack(nums, path):
#             if not nums:
#                 res.append(path)
#                 return
#             for i in range(len(nums)):
#                 backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
#         backtrack(nums, [])
#         return res


nums = [1, 2, 3]
sl = Solution()
print(sl.permute(nums))