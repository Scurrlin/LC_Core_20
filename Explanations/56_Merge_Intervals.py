class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort intervals by their starting values
        intervals.sort(key=lambda pair: pair[0])
        
        # Initialize output with the first interval
        output = [intervals[0]]
        
        # Iterate over each interval in the sorted list
        for start, end in intervals:
            
            # Get the end of the last interval in output
            lastEnd = output[-1][1]
            
            # If current interval overlaps with the last interval in output
            if start <= lastEnd:
                
                # Merge intervals by updating the end of the last interval
                output[-1][1] = max(lastEnd, end)
            else:
                
                # No overlap: add the current interval to output
                output.append([start, end])
        
        # Return the list of merged intervals
        return output

# Time Complexity: O(N log N)
# Space Complexity: O(N)