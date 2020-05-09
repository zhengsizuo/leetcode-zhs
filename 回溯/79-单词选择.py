# class Solution(object):
#     def search(self, board, i, j, word_item):
#         row_length = len(board)-1
#         col_length = len(board[0])-1
#         search_list = list()
#         index_list = list()
#         # 第一行的情况
#         if i==0 and j!=col_length:
#             search_list = [board[i][j+1], board[i+1][j]]
#             index_list = [(i, j+1), (i+1, j)]
#             if j > 0:
#                 search_list.append(board[i][j-1])  #加入左边单元格
#                 index_list.append((i, j-1))
#         if i==0 and j==col_length:
#             search_list = [board[i][j-1], board[i+1][j]]
#             index_list = [(i, j-1), (i+1, j)]
        
#         # 最后一行的情况
#         if i==row_length and j!=col_length:
#             search_list = [board[i][j+1], board[i-1][j]]  #右上
#             index_list = [(i, j+1), (i-1, j)]
#             if j > 0:
#                 search_list.append(board[i][j-1])
#                 index_list.append((i, j-1))
#         if i==row_length and j==col_length:
#             search_list = [board[i][j-1], board[i-1][j]]
#             index_list = [(i, j-1), (i-1, j)]
        
#         # 第一列
#         if j==0 and (0<i<row_length):
#             search_list = [board[i][j+1], board[i-1][j], board[i+1][j]]
#             index_list = [(i, j+1), (i-1, j), (i+1, j)]
#         # 最后一列
#         if j==(col_length) and (0<i<row_length):
#             search_list = [board[i][j-1], board[i-1][j], board[i+1][j]]
#             index_list = [(i, j-1), (i-1, j), (i+1, j)]
#         elif (0<i<row_length) and (0<j<col_length):
#             search_list = [board[i][j+1], board[i+1][j], board[i][j-1], board[i-1][j]]
#             index_list = [(i, j+1), (i+1, j), (i, j-1), (i-1, j)]
        
#         if word_item not in search_list:
#             return False, 0, 0
#         else:
#             for i in range(len(search_list)):
#                 if word_item == search_list[i]:
#                     return True, index_list[i][0], index_list[i][1]
        
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         if len(board)==0 or len(word)==0:
#             return False
        
#         count = 1 #记录遍历次数
#         i_index, j_index= [], []  # 找出所有的首字母，记录到列表中
#         is_used = []  # 标记是否被用过
#         for i in range(len(board)):
#             is_used.append([0]*len(board[0]))
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     i_index.append(i)
#                     j_index.append(j)
#                     # break
#                 count += 1
#         # 遍历整个board数组没找到
#         if count == len(board)*len(board[0]):
#             return False
        
#         w_index = 1
#         k = 0
#         is_used[i_index[k]][j_index[k]] = 1
#         #print(i_index, j_index)
#         print(board[i_index[k]][j_index[k]])
#         while(w_index != len(word)):
#             flag, i, j = self.search(board, i_index[k], j_index[k], word[w_index])
#             print(board[i][j])
#             if not flag or is_used[i][j]:
#                 k += 1  # 如果没找到，从下一个首字母开始找
#                 if k < len(i_index):
#                     print(board[i_index[k]][j_index[k]])
#                     is_used[i_index[k]][j_index[k]] = 1
#                 w_index = 1
#                 # 最后一个首字母还没找到，返回False
#                 if k == len(i_index): 
#                     return False
#             else:
#                 is_used[i][j] = 1
#                 i_index[k], j_index[k] = i, j
#                 w_index += 1
        
#         return True

class Solution(object):
    
    # 定义左右上下四个行走方向
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # 将该元素标记为已使用
                    mark[i][j] = 1
                    if self.backtrack(i, j, mark, board, word[1:]):
                        return True
                    else:
                        # 回溯
                        mark[i][j] = 0
        return False
        
        
    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True
        
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            
            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                # 如果是已经使用过的元素，忽略
                if mark[cur_i][cur_j] == 1:
                    continue
                # 将该元素标记为已使用
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]):
                    return True
                else:
                    # 回溯
                    mark[cur_i][cur_j] = 0
        return False

board =[['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
# word = 'ABCCED'
word = 'SEE'
# word = 'ABCB'
# print(board[1][3]==word[0])

sl = Solution()
print(sl.exist(board, word))