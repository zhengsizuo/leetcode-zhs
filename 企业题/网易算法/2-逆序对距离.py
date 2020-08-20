def Solution(nums):
    dp = [0]*len(nums)
    max_num = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
            dp[i] = dp[i-1]
        else:
            d = 0
            for j in range(i):
                if nums[j] > nums[i]:
                    d += i-j

            dp[i] = dp[i-1] + d

    return dp[-1]


n = int(input())
nums = [int(i) for i in input().split()]
# nums = [1, 3, 4, 2, 5]
print(Solution(nums))