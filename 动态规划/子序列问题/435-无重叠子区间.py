"""套300-最长递增序列，最后两个例子超时"""
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if not intervals: return 0

        intervals.sort(key=lambda x: x[0])
        dp = [1] * len(intervals)
        for i in range(1, len(intervals)):
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return len(intervals) - max(dp)


"""不超时的写法，按结束区间排序，倒着更新，个人觉得很tricky"""
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if not intervals: return 0

        intervals.sort(key=lambda x: x[1])
        print(intervals)
        dp = [1] * len(intervals)
        for i in range(1, len(intervals)):
            for j in range(i-1, -1, -1):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    break
            dp[i] = max(dp[i], dp[i - 1])

        print(dp)
        return len(intervals) - max(dp)


"""贪心算法，照东哥的步骤写的"""
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        if not intervals: return 0

        n = len(intervals)
        valid_set = []
        intervals.sort(key=lambda x: x[1])

        while len(intervals)!=0:
            # 每次选结束时间最小的
            x = intervals.pop(0)
            valid_set.append(x)
            # 剔除与x相交的区间
            for i in intervals.copy():
                if i[0] < x[1]:
                    intervals.remove(i)

        return n - len(valid_set)


intervals = [[1,100],[11,22],[1,11],[2,12]]
intervals = [[1,2], [2,3], [3,4], [1,3]]

# intervals = sorted(intervals, key=lambda intervals: intervals[0])
# print(intervals)
sl = Solution()
print(sl.eraseOverlapIntervals(intervals))