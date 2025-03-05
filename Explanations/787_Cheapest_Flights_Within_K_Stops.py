class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # Initialize dp array with infinity for all nodes, representing unreachable state.
        dp = [float('inf')] * n
        
        # Set the cost to reach the source node to 0.
        dp[src] = 0

        # Perform relaxation for at most k+1 edges (allowing up to k stops).
        for _ in range(k + 1):
            
            # Create a temporary copy of dp for this iteration's updates.
            temp = dp[:]
            
            # Iterate over each flight represented as [u, v, w] (from u to v with cost w).
            for f in flights:
                
                # If the source node of the flight is reachable.
                if dp[f[0]] != float('inf'):
                    
                    # Update the cost to reach the destination node if a cheaper path is found.
                    temp[f[1]] = min(temp[f[1]], dp[f[0]] + f[2])
            
            # Update dp with the newly computed values for the next iteration.
            dp = temp

        # Return the cost to reach dst if it's reachable; otherwise, return -1.
        return dp[dst] if dp[dst] != float('inf') else -1

# Time Complexity: O(K * len(flights))
# Space Complexity: O(N)