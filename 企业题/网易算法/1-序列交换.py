def Solution(nums):
    count = 0  # 统计偶数个数
    for n in nums:
        if n%2 == 0:
            count += 1
    if 0 < count < len(nums):
        print(*(sorted(nums)))

    else:
        print(*nums)


n = int(input())
nums = [int(i) for i in input().split()]
Solution(nums)