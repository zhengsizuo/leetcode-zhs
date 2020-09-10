class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if not intervals: return 0

        n = len(intervals)
        valid_set = []
        intervals.sort(key=lambda x: x[1])

        while len(intervals)!=0:
            x = intervals.pop(0)
            valid_set.append(x)
            # 剔除与x相交的区间
            for i in intervals.copy():
                if i[0] < x[1]:
                    intervals.remove(i)

        return n - len(valid_set)