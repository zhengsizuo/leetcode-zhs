# 简单思路
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1: return x
        y = x
        i = 2
        while y >= 1:
            y = x//i
            # print(y)
            if y**2 <= x and (y+1)**2 > x:
                return y
            i += 1

# 二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1: return x
        left, right = 0, x
        while left<=right:
            mid = (left+right) // 2
            if mid**2<=x and (mid+1)**2>x:
                return mid
            elif mid**2 > x:
                right = mid - 1
            elif (mid+1)**2 <= x:
                left = mid + 1


# 不容易想到的思路，牛顿迭代法
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / sqrtx / solution / x - de - ping - fang - gen - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


x = 20
sl = Solution()
print(sl.mySqrt(x))