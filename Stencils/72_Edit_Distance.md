```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = l(w)
        n = l(w)
        d = [[0] * (n + 1) f _ i r(m + 1)]

        f i i r(1, m + 1):
            d[i][0] = i

        f j i r(1, n + 1):
            d[0][j] = j

        f i i r(1, m + 1):
            f j i r(1, n + 1):
                i w[i - 1] == w[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                e:
                    d[i][j] = m(d[i - 1][j - 1], d[i - 1][j], d[i][j - 1]) + 1

        r d[m][n]

# Time Complexity: O(M * N)
# Space Complexity: O(M * N)
```