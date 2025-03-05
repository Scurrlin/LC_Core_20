```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = 0
        s = []

        f i, h i e(h):
            s = i
            w s a s[-1][1] > h:
                i, h = s.p()
                m = m(m, h * (i - i))
                s = i
            s.a((s, h))

        f i, h i s:
            m = m(m, h * (l(h) - i))
        r m

# Time Complexity: O(N)
# Space Complexity: O(N)
```