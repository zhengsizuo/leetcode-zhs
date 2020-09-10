"""超出时间限制"""
class Solution:
    def largestRectangleArea(self, heights) -> int:
        if not heights:
            return 0

        heights.append(0)
        dp = [0] * len(heights)
        dp[0] = heights[0]

        for i in range(1, len(heights) - 1):
            max_rec = dp[i - 1]
            for j in range(0, i + 1):
                if j > 0:
                    # 如果当前高度比前一个还小，不用计算面积，跳过
                    if heights[j] <= heights[j - 1]:
                        continue

                if (i - j + 1) * min(heights[j:i + 1]) > max_rec:
                    max_rec = (i - j + 1) * min(heights[j:i + 1])

            dp[i] = max_rec

        return dp[-2]


"""单调递增栈的解法，核心思想是找到左边第一个比i小的和右边第一个比i小的"""
class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = [-1]
        area = 0
        heights.append(0)
        for i in range(len(heights)):
            print(stack)
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                area = max(area, h * (i - stack[-1] - 1))
                print("h: ", h, "   Area: ", area)
            stack.append(i)
        heights.pop()

        return area


heights = [2, 1, 5, 6, 2, 3]
sl = Solution()
print(sl.largestRectangleArea(heights))