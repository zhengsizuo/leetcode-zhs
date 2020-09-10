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

"""二分查找，二进制除法"""
def divide(self, dividend: int, divisor: int) -> int:
    sign = (dividend > 0) ^ (divisor > 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    #把除数不断左移，直到它大于被除数
    while dividend >= divisor:
        count += 1
        divisor <<= 1
    result = 0
    while count > 0:
        count -= 1
        divisor >>= 1
        if divisor <= dividend:
            result += 1 << count #这里的移位运算是把二进制（第count+1位上的1）转换为十进制
            dividend -= divisor
    if sign: result = -result
    return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1


# 作者：ysy4869
# 链接：https://leetcode-cn.com/problems/divide-two-integers/solution/xiao-xue-sheng-du-hui-de-lie-shu-shi-suan-chu-fa-b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

dividend = 9
divisor = -3
sl = Solution()
print(sl.divide(dividend, divisor))