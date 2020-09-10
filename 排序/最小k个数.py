"""每次更新最大值，若max和index函数是O(k)复杂度，则总复杂度O(k^2*N)超时"""
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if len(arr) == 0 or k == 0: return []

        arr_k = arr[:k].copy()
        max_val = max(arr_k)
        max_idx = arr_k.index(max_val)
        for i in range(k, len(arr)):
            if arr[i] < max_val:
                arr_k[max_idx] = arr[i]
                max_val = max(arr_k)
                if arr[i] != max_val:
                    max_idx = arr_k.index(max_val)

        return arr_k


"""先对前k个排序，再把比第k个数小的往前冒泡，超时"""


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if len(arr) == 0 or k == 0: return []

        arr_k = arr[:k].copy()
        arr_k.sort()
        for i in range(k, len(arr)):
            if arr[i] < arr_k[-1]:
                arr_k[-1] = arr[i]

                temp_idx = k - 1
                for j in range(k - 2, -1, -1):
                    if arr_k[j] > arr_k[temp_idx]:
                        arr_k[j], arr_k[temp_idx] = arr_k[temp_idx], arr_k[j]
                        temp_idx = j
                    else:
                        break

        return arr_k


"""把前k个数维护成大根堆"""
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if len(arr) == 0 or k == 0: return []

        def max_heapify(heap, heapSize, root):
            # 调整列表中的元素并保证以root为根的堆是一个大根堆
            '''
            给定某个节点的下标root，这个节点的父节点、左子节点、右子节点的下标都可以被计算出来。
            父节点：(root-1)//2
            左子节点：2*root + 1
            右子节点：2*root + 2  即：左子节点 + 1
            '''
            left = 2 * root + 1
            right = left + 1
            larger = root
            if left < heapSize and heap[larger] < heap[left]:
                larger = left
            if right < heapSize and heap[larger] < heap[right]:
                larger = right
            if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的值，这个时候做堆调整操作
                heap[larger], heap[root] = heap[root], heap[larger]
                # 递归的对子树做调整
                max_heapify(heap, heapSize, larger)

        arr_k = arr[:k].copy()
        arr_k.sort(reverse=True)
        for i in range(k, len(arr)):
            if arr[i] < arr_k[0]:
                arr_k[0] = arr[i]
                max_heapify(arr_k, k, 0)  # 调整堆O(logk)

        return arr_k