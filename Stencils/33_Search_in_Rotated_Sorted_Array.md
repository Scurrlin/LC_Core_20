```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, l(n) - 1
        n, t = n, t

        w l <= r:
            m = (l + r)//2
            i t == n[m]:
                r m
            i n[l] <= n[m]:
                i t > n[m] o t < n[l]:
                    l = m + 1
                e:
                    r = m - 1
            e:
                i t < n[m] o t > n[r]:
                    r = m - 1
                e:
                    l = m + 1
        r -1

# Time Complexity: O(log N)
# Space Complexity: O(1)
```