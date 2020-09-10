## 二分查找框架
```C++
int binarySearch(int[] nums, int target) {
    int left = 0, right = ...;

    while(...) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ...
        } else if (nums[mid] < target) {
            left = ...
        } else if (nums[mid] > target) {
            right = ...
        }
    }
    return ...;
}
``` 

## 类型总结 
* 有序数组型：33-搜索排序数组，34-搜索左右区间，240-搜索二维矩阵ii
* 数值型：50-x的平方根，162-寻找峰值，857-可可吃香蕉（典例），410-分割数组的最大值（**困难**）