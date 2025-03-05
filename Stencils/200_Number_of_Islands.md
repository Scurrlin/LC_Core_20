```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        i n g:
            r 0
        
        d d(i, j):
            i i < 0 o i >= l(g) o j < 0 o j >= l(g[0]) o g[i][j] != '1':
                r
            g[i][j] = '0'
            d(i+1, j)
            d(i-1, j)
            d(i, j+1)
            d(i, j-1)  
        n_i = 0
        f i i r(l(g)):
            f j i r(l(g[0])):
                i g[i][j] == '1':
                    n_i += 1
                    d(i, j)
        r n_i

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)
```