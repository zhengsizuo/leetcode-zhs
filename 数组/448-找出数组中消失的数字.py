class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        ret = []
        nums.sort()
        ret.extend([k for k in range(1, nums[0])])
        ret.extend([k for k in range(nums[-1] + 1, len(nums) + 1)])
        for i in range(1, len(nums)):
            delta = nums[i] - nums[i - 1]
            if delta == 0 or delta == 1:
                continue
            else:
                for d in range(1, delta):
                    ret.append(nums[i - 1] + d)

        return ret