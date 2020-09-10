"""跟无重叠区间几乎一回事"""


class Solution:
    def findMinArrowShots(self, points) -> int:
        if not points: return 0

        valid_set = []
        points.sort(key=lambda x: x[1])
        while points:
            x = points.pop(0)
            valid_set.append(x)
            for p in points.copy():
                if p[0] <= x[1]:
                    points.remove(p)

        return len(valid_set)