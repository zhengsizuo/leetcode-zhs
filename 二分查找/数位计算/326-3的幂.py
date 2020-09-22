class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n >= 3:
            x = 1
            while x < n:
                x *= 3
            if x == n:
                return True
            else:
                return False

        else:
            return True if n == 1 else False


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 0
        num = 1
        while num < n:
            num = 3 ** x
            x += 1

        if num == n:
            return True
        else:
            return False