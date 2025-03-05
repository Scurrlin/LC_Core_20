```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = l(h), l(h[0])
        p, a = s(), s()

        d d(r, c, v, p):
            i (
                (r, c) i v
                o r < 0
                o c < 0
                o r == R
                o c == C
                o h[r][c] < p
            ):
                r
            v.a((r, c))
            d(r + 1, c, v, h[r][c])
            d(r - 1, c, v, h[r][c])
            d(r, c + 1, v, h[r][c])
            d(r, c - 1, v, h[r][c])
        f c i r(C):
            d(0, c, p, h[0][c])
            d(R - 1, c, a, h[R - 1][c])
        f r i r(R):
            d(r, 0, p, h[r][0])
            d(r, C - 1, a, h[r][C - 1])
        r = []
        f r i r(R):
            f c i r(C):
                i (r, c) i p a (r, c) i a:
                    r.a([r, c])
        r r

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)
```