def Solution(nums, k):
    is_used = False
    i = 0
    while i < len(nums)-1:
        # print(i)
        if not is_used:
            if nums[i] < max(nums[i+1:i+k+1]):
                is_used = True
            i = i + k

        else:
            if nums[i] > max(nums[i+1:i+k+1]):
                # 如果后k个都比i位置数小，继续跳
                i = i + k
            else:
                return "NO"

    return "YES"


# nums = [1, 8, 2, 3, 4]
# k = 2
T = int(input())
for _ in range(T):
    n, k = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    print(Solution(nums, k))