class Solution(object):
    def sub_merge(self, interval_1, interval_2):
        # 对两个有序区间的合并
        l1, r1 = interval_1[0], interval_1[1]
        l2, r2 = interval_2[0], interval_2[1]
        if r1<l2:
            # 不合并
            return [interval_1, interval_2]
        elif r1>=l2 and r1<r2:
            # interval_1与intervals_2重叠
            return [[l1, r2]]
        elif r1>=l2 and r1>=r2:
            # interval_1包含intervals_2
            return [[l1, r1]]

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return intervals
        # 先按左区间升序排序
        for i in range(len(intervals)-1):
            for j in range(i+1, len(intervals)):
                if intervals[i][0] > intervals[j][0]:
                    temp = intervals[i]
                    intervals[i] = intervals[j]
                    intervals[j] = temp
        
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            sub_ret = self.sub_merge(ret[-1], intervals[i])
            ret.pop()
            ret.extend(sub_ret)
            
        return ret

test_sample = [[1, 4], [0, 1]]
sl = Solution()
print(sl.merge(test_sample))