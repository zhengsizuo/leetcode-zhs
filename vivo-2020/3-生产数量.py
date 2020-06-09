#
#
# @param n int整型 第n天
# @return int整型
#
class Solution:
    def solution(self, n ):
        # write code here
        k = 1
        dp = []
        while len(dp) < n:
            for _ in range(k):
                dp.append(k)
            k += 1

        print(dp[:n])
        return sum(dp[:n])

sl = Solution()
print(sl.solution(11))
