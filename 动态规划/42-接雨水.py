"""动态规划"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total_water, maxLeft, maxRight = 0, 0, 0
        l_max, r_max = [], []

        for h in height:
            if h > maxLeft:
                l_max.append(h)
                maxLeft = h
            else:
                l_max.append(maxLeft)

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