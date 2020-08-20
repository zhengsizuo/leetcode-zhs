import functools
class Solution:
    @functools.lru_cache(None)
    def numDecodings(self, s: str):
        if s[0] == '0': return 0

        if len(s) == 1:
            return 1 if s[0]!='0' else 0
        if len(s) == 2:
            if s[-1]!='0':
                return 2 if int(s) <= 26 else 1
            else:
                return 1 if 0<int(s[0])<=2 else 0

        if int(s[0]) > 2:
            return self.numDecodings(s[1:])

        else:
            if 1<=int(s[:2]) <= 26:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:])


"""可以用标准动态规划解，考虑0非常重要"""

class Solution:
    def numDecodings(self, s: str):
        if s[0] == '0': return 0  # 特例1：以0开头不能解码

        dp = [1] * (len(s) + 1)
        for i in range(1, len(s)):
            if s[i]=='0' and int(s[i-1])>2:
                return 0
            neighbour_s = int(s[i - 1:i + 1])
            if neighbour_s == 0: return 0
            if neighbour_s > 26 or int(s[i - 1]) == 0:
                dp[i + 1] = dp[i]

            else:
                if neighbour_s == 10 or neighbour_s == 20:
                    # 特例2:0前面数字小于等于2可以解码
                    dp[i + 1] = dp[i - 1]
                else:
                    dp[i + 1] = dp[i] + dp[i - 1]

        # print(dp)
        return dp[-1]

sl = Solution()
s = '23226'
s = '101'
print(sl.numDecodings(s))

