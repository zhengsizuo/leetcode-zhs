class Solution:
    def minEatingSpeed(self, piles, H: int) -> int:
        # 特判
        if len(piles) == 1:
            if piles[0] % H == 0:
                return piles[0] // H
            else:
                return piles[0] // H + 1
        def check(mid):
            # 验证mid的取值是否满足时间小于H（二分查找移动指针的条件）
            h = 0
            for n in piles:
                if n % mid == 0:
                    h += n // mid
                else:
                    h += n // mid + 1

            return h <= H

        l, r = 0, max(piles)
        while l < r:
            mid = (l + r) // 2
            print(l, r, mid)
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l


piles = [3, 6, 7, 11]
piles = [30, 11, 23, 4, 20]
H = 5
sl = Solution()
print(sl.minEatingSpeed(piles, H))