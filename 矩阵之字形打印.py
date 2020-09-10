def Solution(rows, cols):
    matrix = [[0]*cols for _ in range(rows)]
    i_plus_j = 0
    item = 1
    while i_plus_j < rows+cols-1:
        if i_plus_j < rows:
            for i in range(i_plus_j, -1, -1):
                j = i_plus_j - i
                if j<0 or j>=cols:
                    break
                # print(i, j, item)
                matrix[i][j] = item
                item += 1

            i_plus_j += 1
        else:
            for i in range(rows-1, -1, -1):
                j = i_plus_j - i
                if j < 0 or j >= cols:
                    break
                # print(i, j, item)
                matrix[i][j] = item
                item += 1

            i_plus_j += 1

    return matrix


rows, cols = 4, 4
print(Solution(rows, cols))