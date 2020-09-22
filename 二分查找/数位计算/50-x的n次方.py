"""简单思路，超时"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = 1
        if n < 0:
            x = 1 / x
            n = -n

        for _ in range(n):
            ret *= x

        return ret


"""二分，分治思想，快速幂算法"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = abs(n)
            x = 1/x
        if n == 0: return 1
        if n == 1: return x
        # 分奇数偶数讨论
        if n % 2 == 0:
            return self.myPow(x, n//2)**2
        else:
            return x*self.myPow(x, n//2)**2


"""二进制角度"""
# 与运算相当于判断当前n是否为奇数，右移一位相当于n//2
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res


