'''
Welcome to vivo !
'''


def solution(N, M):
    queue = list(range(1, N+1))
    ret = []
    pos = 0

    while queue:
        pos = (pos+M-1) % len(queue)
        ret.append(queue.pop(pos))

    return ret


N, M = [int(i) for i in input().split()]
print(solution(N, M))