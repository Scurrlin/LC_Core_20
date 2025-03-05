class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Set the lower bound (1) and upper bound (maximum pile size) for eating speed.
        l, r = 1, max(piles)
        
        # Initialize result with the upper bound, as it's the worst-case eating speed.
        res = r

        # Perform binary search to find the minimum valid eating speed.
        while l <= r:
            
            # Choose the middle speed as the candidate eating speed.
            k = (l + r) // 2
            
            # Initialize total time required to finish all piles at speed k.
            totalTime = 0
            
            # Calculate the time to eat each pile, rounding up since partial hours count as full.
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            
            # If the total time is within the allowed hours, candidate speed is valid.
            if totalTime <= h:
                
                # Update the result to the current candidate speed.
                res = k
                
                # Try finding a smaller valid speed by reducing the upper bound.
                r = k - 1
            else:
                
                # If the candidate speed is too slow, increase the lower bound to search for higher speeds.
                l = k + 1
        
        # Return the minimum eating speed found that allows finishing within h hours.
        return res

# Time Complexity: O(N * log(max(piles)))
# Space Complexity: O(1)