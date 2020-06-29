"""使用内置函数"""


class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            byte = bin(i)[2:]
            res.append(byte.count('1'))

        return res


"""位运算：按照奇偶性动态规划"""