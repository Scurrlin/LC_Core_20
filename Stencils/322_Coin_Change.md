```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = a
        m = [a + 1] * (a + 1)
        m[0] = 0
        
        f i i r(1, a + 1):
            f c i c:
                i i - c >= 0:
                    m[i] = m(m[i], 1 + m[i - c])
        r m[-1] i m[-1] != a + 1 e -1

# Time Complexity: O(amount * len(coins))
# Space Complexity: O(amount)
```