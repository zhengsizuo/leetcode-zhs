# 回溯算法框架
## 伪码
```python
result = []  
def backtrack(path, choice_list):
    if end_condition:
        result.append(path.copy())
    
    for choice in choice_list:
        # 做选择
        将该选择从选择列表移除  # 这一步不一定，得视题目情况而定
        path.append(choice)
        backtrack(path, choice_list)
        # 撤销选择
        路径.remove(选择)
        将该选择再加入选择列表
``` 

## 典型例子
### 基础题
[46-全排列](https://github.com/zhengsizuo/leetcode-zhs/blob/master/%E5%9B%9E%E6%BA%AF/46-%E5%85%A8%E6%8E%92%E5%88%97.py)  
[78-子集](https://github.com/zhengsizuo/leetcode-zhs/blob/master/%E5%9B%9E%E6%BA%AF/78-%E5%AD%90%E9%9B%86.py)  

### 进阶题
[39-组合总和](https://github.com/zhengsizuo/leetcode-zhs/blob/master/%E5%9B%9E%E6%BA%AF/39-%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C.py): 先对选择列表排序，需要考虑不重复的处理  
[79-单词选择](https://github.com/zhengsizuo/leetcode-zhs/blob/master/%E5%9B%9E%E6%BA%AF/79-%E5%8D%95%E8%AF%8D%E9%80%89%E6%8B%A9.py): 设置marked标记是否被访问过  
[51-N皇后](51-N皇后.py)：用绝对值距离判断合理性来剪枝