def Solution(nums):
    pre_sum = [0]*len(nums)
    for i in range(len(nums)):
        pre_sum[i] = sum(nums[:i+1])

    # print(pre_sum)
    dp = [0]*len(nums)
    dp[0] = nums[0]*nums[0]
    for i in range(1, len(nums)):
        max_v = nums[i]*nums[i]
        for j in range(i):
            if j == 0:
                max_v = max(max_v, pre_sum[i]*min(nums[j:i+1]))
            else:
                sum_ = (pre_sum[i]-pre_sum[j-1])
                max_v = max(max_v, sum_ * min(nums[j:i + 1]))
        dp[i] = max_v

    return max(dp)

nums = [6, 5]
n = int(input())
nums = [int(i) for i in input().split()]
print(Solution(nums))