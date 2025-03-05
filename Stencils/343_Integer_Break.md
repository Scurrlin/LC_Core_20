```python
class Solution:
    def integerBreak(self, n: int) -> int:
        d = [0] * (n + 1)
        d[1] = 1
        f i i r(2, n + 1):
            d[i] = -f('i')
            f j i r(1, i):
                d[i] = m(d[i], j * (i - j), j * d[i - j])
        r d[n]

# Time Complexity: O(N^2)
# Space Complexity: O(N)
```