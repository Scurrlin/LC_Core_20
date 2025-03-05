class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # Initialize dictionary 'd' for Prim's algorithm:
        # Map each point (x, y) to its minimum connection cost,
        # with the first point's cost set to 0 and all others to infinity.
        # 'res' will accumulate the total cost of the minimum spanning tree (MST).
        d, res = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}, 0

        # Continue until all points have been connected (i.e., removed from d).
        while d:
            
            # Select the point (x, y) with the smallest connection cost.
            x, y = min(d, key = d.get)
            
            # Add the selected point's connection cost to 'res' and remove it from d.
            res += d.pop((x, y))
            
            # Update the connection cost for each remaining point in d.
            for x1, y1 in d:
                
                # Set the cost to the minimum of its current cost and
                # the Manhattan distance from the newly added point (x, y).
                d[(x1, y1)] = min(d[(x1, y1)], abs(x - x1) + abs(y - y1))
        
        # Return the total cost to connect all points.
        return res

# Time Complexity: O(N^2)
# Space Complexity: O(N)