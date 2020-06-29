"""方法一，类似C++的代码"""
def quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot-1)
        quicksort(arr, pivot+1, right)

def partition(arr, left, right):
    key = arr[left]
    while left < right:
        while left < right and arr[right] > key:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]
    arr[left] = key

    return left

####################################################
# 法二：人生苦短，下面展示一种python实现快排的超简单写法
####################################################
def quecksort_breif(a):
    '''
    NB的python思维实现
    :param a:
    :return:
    '''
    # 确定基条件
    if len(a) < 2:
        return a
    else:
        # 选择基准
        povit = a[0]

        # 确定基准的左边
        less = [i for i in a[1:] if i <= povit]

        # 确定基准的右边
        greater = [i for i in a[1:] if i > povit]

        # 递归调用
        return quecksort_breif(less) + [povit] + quecksort_breif(greater)


if __name__ == "__main__":
    a = [6, 8, 2, 3, 4, 5, 7]
    print("一般思维快排")
    quicksort(a,0,len(a)-1)
    print(a)
    print("python思维快排")
    print(quecksort_breif(a))
