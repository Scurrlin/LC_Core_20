class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Adjacency list for prerequisites
        prereq = {c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # Stores course order (topological sort)
        output = []

        # Tracks visited nodes and cycle detection
        visit, cycle = set(), set()
        def dfs(crs):

            # Cycle detected → not possible to complete courses
            if crs in cycle:
                return False
            
            # Already processed course → no need to revisit
            if crs in visit:
                return True

            # Mark course as being visited in the current path
            cycle.add(crs)

            # Visit all prerequisite courses
            for pre in prereq[crs]:
                if dfs(pre) == False:

                    # Cycle found → return early
                    return False
                
            # Course fully processed, remove from cycle set    
            cycle.remove(crs)

            # Mark as visited
            visit.add(crs)

            # Add course to order (post-order DFS)
            output.append(crs)
            return True
        for c in range(numCourses):

            # If cycle detected, return an empty list
            if dfs(c) == False:
                return []

        # Return topological order    
        return output

# Time Complexity: O(N + E)
# Space Complexity: O(N + E)