directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右搜索

def Solution(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[False]*n for _ in range(m)]

    def dfs(i, j, search_type='water'):
        mark = '*' if search_type=='water' else '#'
        target = 0 if search_type=='water' else 1
        grid[i][j] = mark
        for d in directs:
            next_i = i + d[0]
            next_j = j + d[1]
            if 0<=next_i<m and 0<=next_j<n:
                if grid[next_i][next_j] == target:
                    dfs(next_i, next_j, search_type)
    # 从边界上的0开始搜真正的水域
    for i in range(m):
        if grid[i][0] == 0:
            dfs(i, 0)
        if grid[i][-1] == 0:
            dfs(i, n-1)

    for j in range(n):
        if grid[0][j] == 0:
            dfs(0, j)

    for i in range(m-1):
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j] = 1

    # 从底边陆地开始标记与之相连的1
    dfs(m-1, n-1, 'land')
    # for g in grid:
    #     print(g)

    res = 0
    for i in range(m):
        res += grid[i].count('#')
    return res



# grid = [[1, 0, 0, 1, 0, 0],
#         [0,0,1,0,1,0],
#         [1,1,1,1,1,0],
#         [1,0,0,1,1,1],
#         [1,1,1,1,1,1]]


grid = []
m, n = [int(i) for i in input().split()]
for _ in range(m):
    item = [int(i) for i in input().split()]
    grid.append(item)

print(Solution(grid))
