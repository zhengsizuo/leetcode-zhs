"""使用内置函数"""


class Solution:
    def countBits(self, num: int):
        res = []
        for i in range(num + 1):
            byte = bin(i)[2:]
            res.append(byte.count('1'))

        return res


"""位运算：按照奇偶性动态规划"""
# 在二进制中乘以2相当于左移一位，所以1的个数没有变
# 偶数的末尾是0，下一个奇数比偶数多末尾的1
class Solution:
    def countBits(self, num: int):
        dp = [0]
        for i in range(1, num+1):
            # 如果i为偶数
            if i%2 == 0:
                dp.append(dp[i//2])
            # 如果i为奇数
            else:
                dp.append(dp[i-1]+1)
        return dp


# 作者：xiao-mu-jun
# 链接：https://leetcode-cn.com/problems/counting-bits/solution/338-bi-te-wei-ji-shu-ji-qi-jian-dan-de-jie-fa-by-x/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。