def Solution(n, m, k):
    grid = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            grid[i][j] = (i+1)*(j+1)

    pos = n*m - k
    row = pos // n
    col = pos - row*m

    sort_list = []
    for g in grid:
        sort_list.extend(g)
    sort_list.sort(reverse=True)
    return sort_list[k-1]


n, m, k = [int(i) for i in input().split()]
print(Solution(n, m, k))
