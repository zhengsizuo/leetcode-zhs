class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = 0, 0
        while i < m + n and j < n:
            if nums2[j] < nums1[i]:
                nums1[i + 1:] = nums1[i:-1]
                nums1[i] = nums2[j]
                j += 1
            i += 1

        for k in range(j, n):
            nums1[m + k] = nums2[k]


"""官方题解，简单朴素，合并后排序"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)

