"""动态规划，时间复杂度O(n)，空间复杂度O(n)"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total_water, maxLeft, maxRight = 0, 0, 0
        l_max, r_max = [], []
        # 从左往右扫描，记录每个位置i最左边的最大高度
        for h in height:
            if h > maxLeft:
                l_max.append(h)
                maxLeft = h
            else:
                l_max.append(maxLeft)
        # 从右往左扫描，记录每个位置i最右边的最大高度
        for h in height[::-1]:
            if h > maxRight:
                r_max.append(h)
                maxRight = h
            else:
                r_max.append(maxRight)
        r_max = r_max[::-1]

        for i in range(1, len(height) - 1):
            total_water += min(l_max[i], r_max[i]) - height[i]

        return total_water

"""双指针优化空间复杂度"""