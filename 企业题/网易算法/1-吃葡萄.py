"找规律类型"
def Solution(a, b, c):
    # 讨论其中一个数大于总和的2/3的情况
    half = (a+b+c) // 3 * 2
    for i in [a, b, c]:
        if i>half:
            if i % 2 == 0:
                return i//2
            else:
                return i//2 + 1
    if (a+b+c) % 3 == 0:
        return (a + b + c) // 3
    else:
        return (a + b + c) // 3 + 1


T = int(input())
for _ in range(T):
    a, b, c = [int(i) for i in input().split()]
    print(Solution(a, b, c))


