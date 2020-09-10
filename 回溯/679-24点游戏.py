class Solution:
    def judgePoint24(self, nums) -> bool:
        EPSILON = 10e-6
        ADD, MINUS, MULTIPLY, DIVIDE = 0, 1, 2, 3

        def solve(nums):
            if not nums: return False
            if len(nums) == 1:
                # print(nums[0])
                return abs(nums[0] - 24) < EPSILON

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        for k in range(4):
                            nums_cpy = nums[:]
                            nums_cpy.remove(nums[i])
                            nums_cpy.remove(nums[j])
                            if k == ADD:
                                new_item = nums[i] + nums[j]
                            elif k == MINUS:
                                new_item = nums[i] - nums[j]
                            elif k == MULTIPLY:
                                new_item = nums[i] * nums[j]
                            elif k == DIVIDE:
                                if nums[j] != 0:
                                    new_item = nums[i] / nums[j]

                            nums_cpy.append(new_item)
                            if solve(nums_cpy):
                                return True

            return False

        return solve(nums)


nums = [4, 1, 8, 7]
nums = [1, 1, 7, 7]
sl = Solution()
print(sl.judgePoint24(nums))