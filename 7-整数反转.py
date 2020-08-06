"""巧用字符串"""


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            s = str(x)
            res = int(s[::-1])
        else:
            s = str(abs(x))
            res = -int(s[::-1])

        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res
        else:
            return 0