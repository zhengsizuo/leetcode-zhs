def merge(num_1, num_2):
    result = []
    i, j = 0, 0
    while i < len(num_1) and j < len(num_2):
        if num_1[i] < num_2[j]:
            result.append(num_1[i])
            i = i + 1
        else:
            result.append(num_2[j])
            j = j + 1
    result = result + num_1[i:] + num_2[j:]
    return result


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        final_ret = merge(left, right)
        print(final_ret)

    return final_ret


if __name__ == "__main__":
    a = [6, 8, 2, 3, 4, 5, 7]
    print(mergeSort(a))