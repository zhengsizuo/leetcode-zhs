[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
def numIslands(self, grid: List[List[str]]) -> int:
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

 
 def maxAreaIslands(grid) -> int:
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 上下左右
    m = len(grid)  # 行数
    n = len(grid[0])  # 列数
    if m == 0:
        return 0

    ret = 0

    def dfs(pos, area):
        for dir in dirs:
            next_i = pos[0] + dir[0]
            next_j = pos[1] + dir[1]
            if next_i >= 0 and next_i<m and next_j >= 0 and next_j < n and grid[next_i][next_j]==1:
                grid[next_i][next_j] = 0
                area += 1
                area = dfs([next_i, next_j], area)

        return area

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 0
                area = 1
                area = dfs([i, j], area)
                ret = max(ret, area)

    return ret
