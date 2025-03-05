```python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        r = [r.v]

        d d(r):
            i n r:
                r 0

            l = d(r.l)
            r = d(r.r)
            l = m(l, 0)
            r = m(r, 0)
            r[0] = m(r[0], r.v + l + r)
            r r.v + m(l, r)
        d(r)
        r r[0]

# Time Complexity: O(N)
# Space Complexity: O(N)
```