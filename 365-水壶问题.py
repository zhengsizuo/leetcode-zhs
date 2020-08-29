"""改用栈，保证每种状态只被搜索一次"""
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)] # 初始化两个空壶
        seen = set()

        while stack:
            remain_x, remain_y = stack.pop()  # 栈做DFS，所以FILO
            if remain_x==z or remain_y==z or remain_x+remain_y==z:
                return True
            if (remain_x, remain_y) in seen:
                continue

            seen.add((remain_x, remain_y))
            stack.append((0, remain_y))  # 倒空容量x的水壶
            stack.append((remain_x, 0))  # 倒空容量y的水壶
            stack.append((x, remain_y))  # 装满容量x的水壶
            stack.append((remain_x, y))  # 装满容量y的水壶
            remain = remain_x + remain_y
            if remain > y:
                stack.append((remain_x - (y-remain_y), y))  # 把x水壶的水倒向y
            else:
                stack.append((0, remain))
            if remain > x:
                # 把y水壶的水倒向x
                stack.append((x, remain_y-(x-remain_x)))
            else:
                stack.append((remain, 0))

        return False


"""数学解法，判断z是否是x和y的最大公约数的倍数"""
# https://leetcode-cn.com/problems/water-and-jug-problem/solution/shui-hu-wen-ti-by-leetcode-solution/


import math
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0


sl = Solution()
x, y, z = 3, 5, 4
print(sl.canMeasureWater(x, y, z))