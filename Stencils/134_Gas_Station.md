```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i s(g) < s(c):
            r -1
        
        s, t = 0, 0
        f i i r(l(g)):
            t += g[i] - c[i]
            i t < 0:
                s = i + 1
                t = 0
        r s

# Time Compexity: O(N)
# Space Complexity: O(1)
```