```python
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:            
        r = l(g)
        i r == 0:
            r -1
        c = l(g[0])
        f_c = 0
        r = d()
        
        f r i r(r):
            f c i r(c):
                i g[r][c] == 2:
                    r.a((r, c))
                e g[r][c] == 1:
                    f_c += 1
        
        m_p = 0
        w r a f_c > 0:
            m_p += 1
            f _ i r(l(r)):
                x, y = r.p()
                f d, d i [(1,0), (-1,0), (0,1), (0,-1)]:
                    x, y = x + d, y + d
                    i x < 0 o x == r o y < 0 o y == c:
                        c
                    i g[x][y] == 0 o g[x][y] == 2:
                        c                        
                    f_c -= 1
                    g[x][y] = 2
                    r.a((x, y))

        r m_p i f_c == 0 e -1

# Time Complexity: O(rows * cols)
# Space Complexity: O(rows * cols)
```