"""自己写的递归"""
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

"""官方题解，模拟路径方向"""


class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]: return []

        m = len(matrix)
        n = len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        total = m * n
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 顺时针，右下上左
        idx = 0  # 初始时向右
        i, j = 0, 0  # 初始位置在左上角

        res = []
        for k in range(total):
            visited[i][j] = True
            res.append(matrix[i][j])
            next_i, next_j = i + directions[idx][0], j + directions[idx][1]
            if not (0 <= next_i < m and 0 <= next_j < n and not visited[next_i][next_j]):
                # 如果下一个位置不在合法范围内或者被访问过，变化方向
                idx = (idx + 1) % 4

            i += directions[idx][0]
            j += directions[idx][1]

        return res

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10,11,12],
  [13, 14, 15, 16]
]
# matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
sl = Solution()
print(sl.spiralOrder(matrix))
