class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        def swap(item, nums):
            # 找到nums数组中比item大且最接近的数
            max_res = float('INF')
            j_index = 0
            for j in range(len(nums)):
                if nums[j] > item and nums[j] < max_res:
                    max_res = nums[j]
                    j_index = j

            return j_index

        i = len(nums) - 1
        while i != 0:
            if nums[i] > nums[i - 1]:
                j_index = swap(nums[i - 1], nums[i:])
                j = j_index + i
                temp = nums[j]
                nums[j] = nums[i - 1]
                nums[i - 1] = temp
                # 交换完之后把nums[i:]按升序排列
                nums[i:] = sorted(nums[i:])
                break

            else:
                i = i - 1

        # i被减到0，原数组为降序排列
        if i == 0:
            nums.sort()


nums = [1, 3, 2]
sl = Solution()
sl.nextPermutation(nums)
print(nums)