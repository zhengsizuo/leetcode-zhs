class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        residual = []
        while num > 1:
            residual.append(num % 2)
            num = num // 2
        residual.append(num % 2)
        return residual.count(1)


# num = 5
# residual = []
# while num > 1:
#     residual.append(num % 2)
#     num = num // 2
# residual.append(num % 2)
# print(residual.count(1))