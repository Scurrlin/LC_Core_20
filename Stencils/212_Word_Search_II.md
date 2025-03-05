```python
class TrieNode:
    def __init__(self):
        s.c = {}
        s.i = F
        s.r = 0

    def addWord(self, word):
        c = s
        c.r += 1
        f c i w:
            i c n i c.c:
                c.c[c] = T()
            c = c.c[c]
            c.r += 1
        c.i = T

    def removeWord(self, word):
        c = s
        c.r -= 1
        f c i w:
            i c i c.c:
                c = c.c[c]
                c.r -= 1

# Time Complexity: O(L)
# Space Complexity: O(1)
```