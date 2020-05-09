"""双指针，移动较小的那一端"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = min(height[left], height[right]) * (right - left)

        while (left != right):
            if height[left] < height[right]:
                left += 1
                max_area = min(height[left], height[right]) * (right - left)
                if max_area > res:
                    res = max_area

            else:
                right -= 1
                max_area = min(height[left], height[right]) * (right - left)
                if max_area > res:
                    res = max_area

        return res