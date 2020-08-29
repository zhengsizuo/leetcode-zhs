"""把原数组翻倍，继续套用单调栈模板"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums  # 原数组翻倍
        stack = []
        res = [0] * len(nums2)
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            res[i] = -1 if not stack else stack[-1]
            stack.append(nums2[i])

        return res[:len(nums)]


"""也可以模拟循环数组取余数"""