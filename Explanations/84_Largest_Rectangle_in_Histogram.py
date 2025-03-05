class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # Initialize maximum area found
        maxArea = 0

        # Stack to store pairs (start index, height)
        stack = []

        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            
            # Set the start index for the current bar
            start = i

            # While there are bars in the stack and the last bar's height is greater than current height
            while stack and stack[-1][1] > h:

                # Remove the last bar from the stack
                index, height = stack.pop()

                # Update maxArea using the popped bar's height
                maxArea = max(maxArea, height * (i - index))

                # Update start to extend the rectangle leftwards
                start = index

            # Add the current bar with its valid start index to the stack    
            stack.append((start, h))

        # Process remaining bars in the stack after iterating through all heights
        for i, h in stack:

            # Calculate area from index i to the end of the histogram
            maxArea = max(maxArea, h * (len(heights) - i))

        # Return the largest rectangle area found    
        return maxArea

# Time Complexity: O(N)
# Space Complexity: O(N)