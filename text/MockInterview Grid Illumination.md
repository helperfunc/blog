模拟面试视频
https://www.youtube.com/watch?v=MlhXpsvODb8

leetcode 题
https://leetcode.com/problems/grid-illumination/

## 印象最深的是三点：
1. 面试者首先问 n 的范围，再问 lamps 是否有重复的坐标。很快想到了要用 hash 去重，并且想到了不能在循环过程中改变 hashset 的 value，要另外开辟一个 hashset 作为判断灯是否被关掉了。

2. hash作为缓存，对 Java 而言，list是一个内存地址，不能用作 key。面试者很快就想到了用 x * n + y 的计算作为 key，
反向求 x和 y的计算也很简单。
```
x = key // n
y = key - x
```
3. 面试官问道，如果 lamps 很大，该如何优化？
面试者先想到了，用 n 大小的两个向量，存行和列的 lamps 的数量。然后再去想该怎么存对角线的 lamps 数量。
这时，面试官提示，假设给定 (x, y)，如何知道它处于那条对角线？
然后面试官给了一个具体的例子
```
(x, y)
  0 1 2 3
0 0 0 0 0
1 0 1 1 0
2 0 0 0 0
3 0 0 0 0
```

面试者首先想到了对角线向量的大小，应该是 2 * n - 1
然后再想每条对角线内的元素有何共同特征。右上对角线中每条对角线的共同特征是 x + y 都为同一个数。

那么该如何确定左下对角线元素的共同特征呢？
这时面试者，非常快的就想到了。右上和左下刚好是列元素的一个翻转。例子中的3对应0，0对应3，那么就应该是 x + y 对应 x + n - 1 - y。


面试者忽视的地方，如何更新 query 周围8个grid中可能有的灯？

## 用到的算法
模拟法

## 算法实现中值得注意的点
如果下面的 count_row 等4个缓存 hash 换成 list，对于大数据
```
1 <= n <= 1000000000
0 <= lamps.length <= 20000
0 <= queries.length <= 20000
```
会超时。

```python
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 对 lamps 去重，python 可以用 tuple 作为 key
        lamps_set = {(r, c) for r, c in lamps}
        
        # 每行，每列，每条对角线的灯的数目缓存，用于快速判断 query 对应的坐标是否被照亮
        count_row, count_col = {}, {}
        count_right_diag, count_left_diag = {}, {}
        for r, c in lamps_set:
            count_row[r] = count_row.get(r, 0) + 1
            count_col[c] = count_col.get(c, 0) + 1
            count_right_diag[r + c] = count_right_diag.get(r + c, 0) + 1
            count_left_diag[r + n - 1 - c] = count_left_diag.get(r + n - 1 -c, 0) + 1
            
        result = []
        for qr, qc in queries:
            if self.isIlluminated(count_row, count_col, count_right_diag, count_left_diag, qr, qc, n):
                result.append(1)
            else:
                result.append(0)
            
            # 熄灭周围的 8 个 cell 中可能的灯
            for r, c in product(range(qr - 1, qr + 2), range(qc - 1, qc + 2)):
                if (r, c) in lamps_set:
                    lamps_set.remove((r, c))
                    count_row[r] -= 1
                    count_col[c] -= 1
                    count_right_diag[r + c] -= 1
                    count_left_diag[r + n - 1 - c] -= 1
            
        return result
    
    def isIlluminated(self, count_row: List[int], count_col: List[int], count_rdiag: List[int], count_ldiag: List[int], r: int, c: int, n: int) -> bool:
        return count_row.get(r, 0) or count_col.get(c, 0) or count_rdiag.get(r + c, 0) or count_ldiag.get(r + n - 1 - c, 0)
```
