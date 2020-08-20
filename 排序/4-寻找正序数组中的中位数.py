"""归并排序的应用"""


class Solution:
    def merge(self, num_1, num_2):
        ret = []
        i, j = 0, 0
        while i < len(num_1) and j < len(num_2):
            if num_1[i] <= num_2[j]:
                ret.append(num_1[i])
                i = i + 1
            else:
                ret.append(num_2[j])
                j = j + 1

        return ret + num_1[i:] + num_2[j:]

    def findMid(self, nums):
        mid = len(nums) // 2
        if len(nums) % 2 != 0:
            return nums[mid]
        else:
            return (nums[mid] + nums[mid - 1]) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return self.findMid(nums2)
        if not nums2:
            return self.findMid(nums1)

        nums = self.merge(nums1, nums2)
        return self.findMid(nums)