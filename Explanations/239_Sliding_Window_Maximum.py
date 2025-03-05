class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Initialize the output list to store maximum values for each sliding window.        
        output = []
        
        # Initialize a deque to keep indices of potential max elements in the current window.
        q = collections.deque()
        
        # Initialize left (l) and right (r) pointers for the sliding window.
        l = r = 0

        # Iterate while the right pointer is within the bounds of nums.
        while r < len(nums):
            
            # Remove indices from the deque if their corresponding values are less than nums[r].
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # Append the current index r to the deque.
            q.append(r)
            
            # If the left pointer is beyond the index at the front of the deque, remove that index.
            if l > q[0]:
                q.popleft()
            
            # Once we have a complete window of size k, record the maximum (at the front of the deque).
            if (r + 1) >= k:
                output.append(nums[q[0]])
                
                # Move the left pointer to slide the window forward.
                l += 1
            
            # Move the right pointer to expand the window.
            r += 1
        
        # Return the list of maximum values for each window.
        return output

# Time Complexity: O(N)
# Space Complexity: O(N)