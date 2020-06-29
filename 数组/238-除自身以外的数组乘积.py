"""超出时间限制"""
class Solution:
    def productExceptSelf(self, nums):
        from functools import reduce
        res = []
        guard = nums.pop(0)
        top = guard
        while nums[0] != top:
            ln = reduce(lambda x, y: x*y, nums)
            res.append(ln)

            nums.append(guard)
            guard = nums.pop(0)

        ln = reduce(lambda x, y: x*y, nums)
        res.append(ln)
        return res


"""O(N)时间复杂度，O(1)空间复杂度，思想是维护位置i左右两边的数组"""

class Solution:
    def productExceptSelf(self, nums):
        p = 1
        L, R = [p], [p]
        for i in range(1, len(nums)):
            p *= nums[i - 1]
            L.append(p)

        p = 1
        R[0] *= L[-1]
        # 从后往前算右数组的时候顺便计算乘积
        for i in reversed(range(len(nums) - 1)):
            p *= nums[i + 1]
            R.insert(0, p * L[i])

        return R


nums = [1, 2, 3, 4]
sl = Solution()
print(sl.productExceptSelf(nums))