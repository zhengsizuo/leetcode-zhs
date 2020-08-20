"""归并排序的应用"""
class Solution:
    def __init__(self):
        self.cnt = 0

    def merge(self, num_1, num_2):
        ret = []
        i, j = 0, 0
        while i < len(num_1) and j < len(num_2):
            if num_1[i] <= num_2[j]:
                ret.append(num_1[i])
                i = i + 1
            else:
                self.cnt += len(num_1) - i
                ret.append(num_2[j])
                j = j + 1

        return ret + num_1[i:] + num_2[j:]

    def mergeSort(self, nums):
        if not nums: return
        if len(nums) == 1:
            return nums

        else:
            mid = len(nums) // 2
            left = self.mergeSort(nums[:mid])
            right = self.mergeSort(nums[mid:])
            return self.merge(left, right)

    def reversePairs(self, nums) -> int:
        self.mergeSort(nums)

        return self.cnt


nums = [7, 5, 6, 4]
sl = Solution()
print(sl.reversePairs(nums))



