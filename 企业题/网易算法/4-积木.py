def Solution(nums, m):
    if len(nums) == 1:
        return "YES"
    for i in range(len(nums)):
        if (nums[i]+1) < i:
            return "NO"

    if nums[0] >= nums[1]:
        m += 1

    for i in range(1, len(nums)-1):
        if nums[i-1] < nums[i] < nums[i+1]:
            continue
        if nums[i] > nums[i+1]:
            m += 1  # 取一块
        if nums[i] == nums[i-1]:
            m -= 1  # 放一块

    if nums[-1] >= nums[-2] and m>0:
        return "YES"
    else:
        return "NO"


# nums = [0, 0, 1, 3, 1]
# m = 2
T = int(input())
for _ in range(T):
    n, m = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    print(Solution(nums, m))
