import functools
@functools.lru_cache(None)
def Solution(N):
    """
        N: 盒子数目
        return: 最少操作数
    """
    if N<=1:
        return N
    dp = [0]*(N+1)
    dp[1] = 1
    for i in range(2, N+1):
        if i%2 == 0:
            dp[i] = dp[i//2] + 1
        else:
            dp[i] = dp[(i-1)//2] + 1
    return dp[-1]

print(Solution(29))
# import sys
# input_list = []
# T = 0
# for i, line in enumerate(sys.stdin):
#     if i==0:
#         T = int(line)
#     input_list.append(int(line))
#     if i >= T:
#         break

# input_list = []
# T = int(input())
# for _ in range(T):
#     input_list.append(int(input()))
# for i in range(len(input_list)):
#     print(Solution(input_list[i]))