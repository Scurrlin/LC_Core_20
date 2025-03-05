class Solution:
    def trap(self, height: List[int]) -> int:

        # Alias for readability
        h = height

        # If the height list is empty, no water can be trapped
        if not h:
            return 0

        # Initialize left and right pointers at start and end
        l, r = 0, len(h) - 1
        
        # Set initial max heights from the left and right
        leftMax, rightMax = h[l], h[r]
        
        # Initialize result to store total trapped water
        res = 0
        
        # Process the array until pointers meet
        while l < r:

            # If left max is smaller, process left side
            if leftMax < rightMax:

                # Move left pointer to the right
                l += 1

                # Update left maximum
                leftMax = max(leftMax, h[l])

                # Add trapped water at current position
                res += leftMax - h[l]
            else:

                # Move right pointer to the left
                r -= 1

                # Update right maximum
                rightMax = max(rightMax, h[r])

                # Add trapped water at current position
                res += rightMax - h[r]
        return res

# Time Complexity: O(N)
# Space Complexity: O(1)