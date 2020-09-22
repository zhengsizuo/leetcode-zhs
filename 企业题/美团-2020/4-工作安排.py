def Solution(tasks):
    if not tasks: return 0

    n = len(tasks)
    dp = [0]*(n+1)
    dp[1] = tasks[0][0]
    for i in range(2, n+1):
        t = tasks[i-1]
        dp[i] = max(dp[i-1]+t[0], dp[i-2]+t[1])

    return dp[-1]

N = int(input())
tasks = []
for _ in range(N):
    t = [int(i) for i in input().split()]
    tasks.append(t)

# tasks = [[10, 5], [1, 50], [10, 5], [10, 1]]
print(Solution(tasks))
