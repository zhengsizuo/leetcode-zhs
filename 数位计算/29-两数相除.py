"""化为加法，超时严重"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return 0
        cnt = 0
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        sum_ = divisor_abs
        while sum_ <= dividend_abs:
            sum_ += divisor_abs
            cnt += 1
            print(cnt, sum_)

        if dividend * divisor > 0:
            return cnt

        else:
            return -cnt


dividend = 9
divisor = -3
sl = Solution()
print(sl.divide(dividend, divisor))