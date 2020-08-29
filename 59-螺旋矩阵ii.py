class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        order = list(range(1, n ** 2 + 1))

        mat = [[0] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 顺时针，右下上左
        idx = 0  # 初始时向右
        i, j = 0, 0  # 初始位置在左上角

        for k in range(n ** 2):
            mat[i][j] = order[k]
            visited[i][j] = True
            next_i, next_j = i + directions[idx][0], j + directions[idx][1]
            if not (0 <= next_i < n and 0 <= next_j < n and not visited[next_i][next_j]):
                # 如果下一个位置不在合法范围内或者被访问过，变化方向
                idx = (idx + 1) % 4

            i += directions[idx][0]
            j += directions[idx][1]

        return mat