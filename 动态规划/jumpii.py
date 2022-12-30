nums = [2, 3, 1, 1, 4]

def jump_ii(nums):
    dp = [0]*len(nums)
    for i in range(1, len(nums)):
        min_cnt = float('inf')
        for j in range(i):
            if nums[j] >= i - j:
                min_cnt = min(min_cnt, dp[j])
        dp[i] = min_cnt + 1

    return dp[-1]


print(jump_ii(nums))