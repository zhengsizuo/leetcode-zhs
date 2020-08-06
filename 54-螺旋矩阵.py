class Solution:
    def spiralOrder(self, matrix):
        res = []

        def search_outside(matrix):
            if not matrix or not matrix[0]:
                return res
            m = len(matrix)
            n = len(matrix[0])
            for j in range(n):
                res.append(matrix[0][j])
            for i in range(1, m):
                res.append(matrix[i][-1])
            for j in range(n - 2, -1, -1):
                if m == 1: break  # 处理特殊情况，如果只有一行就不往回遍历
                res.append(matrix[-1][j])
            for i in range(m - 2, 0, -1):
                if n == 1: break  # 如果只有一列就不往上回溯
                res.append(matrix[i][0])

            new_mat = [mat[1:-1] for mat in matrix[1:-1]]
            return search_outside(new_mat)

        return search_outside(matrix)

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10,11,12],
  [13, 14, 15, 16]
]
matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
sl = Solution()
print(sl.spiralOrder(matrix))
