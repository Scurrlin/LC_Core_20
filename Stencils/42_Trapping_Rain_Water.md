```python
class Solution:
    def trap(self, height: List[int]) -> int:
        h = h
        i n h:
            r 0

        l, r = 0, l(h) - 1
        l, r = h[l], h[r]
        r = 0
        w l < r:
            i l < r:
                l += 1
                l = m(l, h[l])
                r += l - h[l]
            e:
                r -= 1
                r = m(r, h[r])
                r += r - h[r]
        r r

# Time Complexity: O(N)
# Space Complexity: O(1)
```