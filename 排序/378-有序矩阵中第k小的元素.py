class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        def heapfy(heap, heapsize, root):
            # 小根堆调整函数
            left = 2 * root + 1
            right = left + 1
            smaller = root
            if left < heapsize and heap[left][0] < heap[root][0]:
                smaller = left
            if right < heapsize and heap[right][0] < heap[root][0]:
                smaller = right

            if smaller != root:
                heap[smaller], heap[root] = heap[root], heap[smaller]
                heapfy(heap, heapsize, smaller)

        def build_min_heap(heap):
            # 构造一个堆，将堆中所有数据重新排序
            heapSize = len(heap)
            for i in range((heapSize - 2) // 2, -1, -1):  # 自底向上建堆
                heapfy(heap, heapSize, i)

        heap = []
        n = len(matrix)
        for i in range(n):
            heap.append([matrix[i][0], i, 0])

        while k != 1:
            val, x, y = heap.pop(0)
            k -= 1
            #print(k, heap)
            if y != n - 1:
                heap.append([matrix[x][y + 1], x, y + 1])
                # print(heap)
                build_min_heap(heap)

        return heap[0][0]

"""官方题解，注释"""

import heapq
class Solution2:
    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix)  # 注：题目中这个矩阵是n*n的，所以长宽都是n

        pq = [(matrix[i][0], i, 0) for i in range(n)]  # 取出第一列候选人
        # matrix[i][0]是具体的值，后面的(i,0)是在记录候选人在矩阵中的位置，方便每次右移添加下一个候选人

        heapq.heapify(pq)  # 变成一个heap

        for i in range(k - 1):  # 一共弹k次：这里k-1次，return的时候1次
            num, x, y = heapq.heappop(pq)  # 弹出候选人里最小一个
            if y != n - 1:  # 如果这一行还没被弹完
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))  # 加入这一行的下一个候选人

        return heapq.heappop(pq)[0]


# 作者：xiao - yan - gou
# 链接：https: // leetcode - cn.com / problems / kth - smallest - element - in -a - sorted - matrix / solution / shi - yong - dui - heapde - si - lu - xiang - jie - ling - fu - python /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
k = 5

sl = Solution()
print(sl.kthSmallest(matrix, k))