def Solution(s1, s2):
    n = len(s2) if len(s1)<len(s2) else len(s1)
    i = 0
    while s1[i] == s2[i] and i<n:
        i += 1

    return i
    # dp = [[0]*n for _ in range(m)]
    # dp[0][0] = 1 if s1[0]==s2[0] else 0
    # for j in range(n):
    #     dp[0][j] = dp[0][j-1] if s1[0] == s2[j] else 1
    # for i in range(m):
    #     dp[i][0] = dp[i-1][0] if s1[i] == s2[0] else 1



n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

import sys
for line in sys.stdin:
    a = line.split()
    a1, a2 = [int(x) for x in a]
    print(Solution(strings[a1-1], strings[a2-1]))