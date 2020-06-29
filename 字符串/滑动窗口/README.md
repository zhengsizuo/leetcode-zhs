# 滑动窗口模板 
## 要点 
- 设置左右指针left，right
- 设置需要匹配的哈希表need，滑动窗口哈希表window
```C++
/* 滑动窗口算法框架 */
void slidingWindow(string s, string t) {
    unordered_map<char, int> need, window;
    for (char c : t) need[c]++;

    int left = 0, right = 0;
    int valid = 0; 
    while (right < s.size()) {
        // c 是将移入窗口的字符
        char c = s[right];
        // 右移窗口
        right++;
        // 进行窗口内数据的一系列更新
        ...

        /*** debug 输出的位置 ***/
        printf("window: [%d, %d)\n", left, right);
        /********************/

        // 判断左侧窗口是否要收缩
        while (window needs shrink) {
            // d 是将移出窗口的字符
            char d = s[left];
            // 左移窗口
            left++;
            // 进行窗口内数据的一系列更新
            ...
        }
    }
}
```  
## 代表题目
3-最长无重复子串（中等）  
438-找字符串字母异位词（中等）  
76-最小覆盖子串（困难，难点在于设置一个match变量来判断操作条件）  
