```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        o = []
        q = c.d()
        l = r = 0

        w r < l(n):
            w q a n[q[-1]] < n[r]:
                q.p()
            q.a(r)
            i l > q[0]:
                q.p()
            i (r + 1) >= k:
                o.a(n[q[0]])
                l += 1
            r += 1
        r o

# Time Complexity: O(N)
# Space Complexity: O(N)
```