```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = [f('i')] * n
        d[s] = 0

        f _ i r(k + 1):
            t = d[:]
            f f i f:
                i d[f[0]] != f('i'):
                    t[f[1]] = m(t[f[1]], d[f[0]] + f[2])
            d = t
        r d[d] i d[d] != f('i') e -1

# Time Complexity: O(K * len(flights))
# Space Complexity: O(N)
```