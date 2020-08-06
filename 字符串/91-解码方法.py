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

"""可以用标准动态规划解"""


sl = Solution()
s = '23226'
print(sl.numDecodings(s))

