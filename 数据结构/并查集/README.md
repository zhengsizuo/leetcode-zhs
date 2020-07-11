# 并查集
并查集的关键在于定义两个API函数：连通任意两个节点的union函数和查找节点的根节点函数find  
## C++ API
参考[laluladong公众号](https://labuladong.gitbook.io/algo/gao-pin-mian-shi-xi-lie/unionfind-suan-fa-xiang-jie)  
```C++
class UF {
    // 连通分量个数
    private int count;
    // 存储一棵树
    private int[] parent;
    // 记录树的“重量”
    private int[] size;

    public UF(int n) {
        this.count = n;
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ)
            return;

        // 小树接到大树下面，较平衡
        if (size[rootP] > size[rootQ]) {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        } else {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        }
        count--;
    }

    public boolean connected(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        return rootP == rootQ;
    }

    private int find(int x) {
        while (parent[x] != x) {
            // 进行路径压缩, 指向父节点的父节点
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    public int count() {
        return count;
    }
}
```

## Python API
```python
class UF:
    def __init__(self, n):
        self.parent = {x: x for x in range(n)}
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        self.parent[root_p] = root_q  # 将root_p树接在根节点q下
        
    def find(self, x):
        # 查找x的根节点
        if x == self.parent[x]:
            return x
        return self.find(self.parent[x])
        
            
```