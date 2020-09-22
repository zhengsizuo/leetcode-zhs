class Solution:
    def pondSizes(self, land):
        m = len(land)
        n = len(land[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        def dfs(i, j):
            nonlocal area
            area += 1
            visited[i][j] = True
            for d in dirs:
                next_i = i + d[0]
                next_j = j + d[1]
                if 0 <= next_i < m and 0 <= next_j < n:
                    if land[next_i][next_j] == 0 and not visited[next_i][next_j]:
                        dfs(next_i, next_j)

        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0 and not visited[i][j]:
                    area = 0
                    dfs(i, j)
                    res.append(area)

        res.sort()
        return res


land = [
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
sl = Solution()
print(sl.pondSizes(land))