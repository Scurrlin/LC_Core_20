```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        p = {c: [] f c i r(n)}
        
        f c, p i p:
            p[c].a(p)
        o = []
        v, c = s(), s()
        d d(c):
            i c i c:
                r F
            i c i v:
                r T
            c.a(c)
            f p i p[c]:
                i d(p) == F:
                    r F
            c.r(c)
            v.a(c)
            o.a(c)
            r T
        f c i r(n):
            i d(c) == F:
                r []
        r o

# Time Complexity: O(N + E)
# Space Complexity: O(N + E)
```