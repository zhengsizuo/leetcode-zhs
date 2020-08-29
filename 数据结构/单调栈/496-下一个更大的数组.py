class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res2 = [0] * len(nums2)
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            res2[i] = -1 if not stack else stack[-1]
            stack.append(nums2[i])

        res1 = []
        for n in nums1:
            idx = nums2.index(n)
            res1.append(res2[idx])

        return res1