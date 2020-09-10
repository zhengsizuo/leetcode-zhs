class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]: return

        m = len(matrix)
        n = len(matrix[0])
        zeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append([i, j])

        for pos in zeros:
            for j in range(n):
                matrix[pos[0]][j] = 0
            for i in range(m):
                matrix[i][pos[1]] = 0