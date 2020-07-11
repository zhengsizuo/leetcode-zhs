#
# 输入一个整形数值，返回一个整形值
# @param n int整型 m>9
# @return int整型
#
class Solution:
    def solution(self , n ):
        # write code here
        if n < 10: return n+10

        ret = 0
        base = 0
        for i in reversed(range(2, 10)):
            while n % i == 0:
                ret += i*10**base
                base += 1
                n = n // i
                # print(n)

        if n>1: return -1  # 不能分解完，返回-1

        return ret


sl = Solution()
print(sl.solution(100))
print(sl.solution(108))
print(sl.solution(11))