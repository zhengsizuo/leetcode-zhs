"""回溯说我超时"""
directs = [(0,1), (1,0)]
def Solution(x, y, bosses):
    res = 0
    target = (x, y)
    def backtrack(cur_pos):
        nonlocal res
        if cur_pos == target:
            res += 1
            return

        for d in directs:
            next_i = cur_pos[0] + d[0]
            next_j = cur_pos[1] + d[1]
            if 0<=next_i<x+1 and 0<=next_j<y+1 and (next_i, next_j) not in bosses:
                backtrack((next_i, next_j))

    backtrack((0, 0))
    return res


"""动态规划"""
def Solution(x, y, bosses):
    dp = [[0]*(x+1) for _ in range(y+1)]
    dp[0][0] = 1
    for j in range(1, y+1):
        if (0, j) not in bosses:
            dp[0][j] = dp[0][j-1]
    for i in range(1, x+1):
        if (i, 0) not in bosses:
            dp[i][0] = dp[i-1][0]

    for i in range(1, x+1):
        for j in range(1, y+1):
            if (i, j) not in bosses:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]

# x, y = 3, 3
# bosses = [(1, 1), (2, 2)]
bosses = []
x, y, n = [int(i) for i in input().split()]
for _ in range(n):
    xi, yi = [int(i) for i in input().split()]
    bosses.append((xi, yi))
print(Solution(x, y, bosses))

