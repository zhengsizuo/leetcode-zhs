"""两遍哈希法"""
class Solution:
    def twoSum(self, nums, target: int):
        if not nums: return []

        hash_set = {}
        for i, n in enumerate(nums):
            hash_set[n] = i

        # print(hash_set)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_set and hash_set[complement]!=i:
                return [i, hash_set[complement]]


"""排序加双指针，不适合返回索引的情况"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums: return []

        new_nums = sorted(nums)
        l = 0
        r = len(new_nums) - 1
        res_n = []
        while l < r:
            sum_ = new_nums[l] + new_nums[r]
            if sum_ < target:
                l += 1
            elif sum_ > target:
                r -= 1
            elif sum_ == target:
                res_n.append(new_nums[l])
                res_n.append(new_nums[r])
                break

        for i in range(len(res_n)):
            res_n[i] = nums.index(res_n[i])

        return res_n

nums = [3, 3]
target = 6
sl = Solution()
print(sl.twoSum(nums, target))