# 动态规划思路
## 三要素
1. 重叠子问题  
2. 最优子结构——子问题相互独立    
3. 状态转移方程  
- 前两个条件是运用动态规划的前提，最后一个条件是实现的关键

## 一般步骤
两种方式：带备忘录的自顶向下、自底向上（推荐）  
这两种方式的解题流程是一样的：  
- 明确“状态” --> 定义dp数组/函数的含义 --> 明确“选择” --> 明确base case  
- 其中，自顶向下一般使用dp函数，base case是递归结束的条件；自底向上一般使用dp数组，base case是数组的前几个元素  

## 类型
* 0-1背包：416-分割等和子集、494-目标和  
[0-1背包代码框架](https://mp.weixin.qq.com/s/RXfnhSpVBmVneQjDSUSAVQ)
```python
def Solution(N, W, w_t, val): 
    # w_t表示背包重量数组，val表示背包对应的价值
    # dp[N][W]：表示装了N件物品的、重量W的价值 
    dp = [[0]*(W+1) for _ in range(N+1)] 
    
    for i in range(1, N+1):
        for w in range(1, W+1):
            if w-w_t[i-1] < 0:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_t[i-1]]+val[i-1]) 
    
    return dp[N][W]

```
* 字符串定义二维数组：72-编辑距离、10-正则表达式、516-回文子序列
  