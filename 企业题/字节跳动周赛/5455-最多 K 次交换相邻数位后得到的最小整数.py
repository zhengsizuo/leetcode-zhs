"""暴力递归"""


class Solution:
    def __init__(self):
        self.res = str()

    def minInteger(self, num: str, k: int) -> str:
        if k == 0:
            return self.res + num

        min_s = min(num)
        i = num.index(min_s)
        if k >= i:
            self.res += min_s
            self.minInteger(num[:i] + num[i + 1:], k - i)

        if k < i:
            max_s = max(num)
            j = num.index(max_s)
            if j == len(num) - 1:
                self.minInteger(self.num[:j], k)

            temp = '' * len(num)
            num[j:j + k] = num[j + 1:j + k + 1]
            num[j + k] = max_s

            return self.res + num


"""线段树优化"""