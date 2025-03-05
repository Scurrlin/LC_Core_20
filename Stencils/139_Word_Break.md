```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = l(s)
        d = [F] * (n + 1)
        d[0] = T
        m_l = m(m(l, w))

        f i i r(1, n + 1):
            f j i r(i - 1, m(i - m_l - 1, -1), -1):
                i d[j] a s[j:i] i w:
                    d[i] = T
                    b
        r d[n]

# Time Complexity: O(N * max_len)
# Space Complexity: O(N)
```