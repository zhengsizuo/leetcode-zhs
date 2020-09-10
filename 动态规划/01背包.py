def Solution(N, W, w_t, val):
    # w_t表示背包重量数组，val表示背包对应的价值
    # dp[N][W]：表示装了N件物品的、重量W的价值
    dp = [[0] * (W+1) for _ in range(N+1)]

    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if w - w_t[i - 1] < 0:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w],  # 不装进背包
                               dp[i - 1][w - w_t[i - 1]] + val[i - 1])  # 装进背包
            print(i, w, dp[i][w])

    return dp[N][W]


N, W = 3, 4
w_t = [2, 1, 3]
val = [4, 2, 3]
print(Solution(N, W, w_t, val))