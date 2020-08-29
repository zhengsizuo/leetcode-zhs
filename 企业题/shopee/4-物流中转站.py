"""暴力，也不超时？？"""
def Solution(board):
    m = len(board)
    n = len(board[0])

    space_pos = []
    house_pos = []
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                house_pos.append([i, j])
            else:
                space_pos.append([i, j])

    if not space_pos: return -1

    min_distance = float('inf')
    for space in space_pos:
        distance = 0
        x, y = space[0], space[1]
        for house in house_pos:
            i, j = house[0], house[1]
            distance += abs(x-i) + abs(y-j)

        if distance < min_distance:
            min_distance = distance

    return min_distance


n = int(input())
board = []
for _ in range(n):
    board.append([int(i) for i in input().split()])

print(Solution(board))


