class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Initialize left and right pointers
        l, r = 0, len(nums) - 1

        # Alias for readability
        n, t = nums, target

        while l <= r:

            # Find the middle index
            m = (l + r) // 2
            if t == n[m]:

                # Target found, return index
                return m

            # Determine if the left half is sorted
            if n[l] <= n[m]:

                # Target is outside the sorted left half, search right
                if t > n[m] or t < n[l]:
                    l = m + 1

                # Target is inside the sorted left half, search left    
                else:
                    r = m - 1
            else:

                # Target is outside the sorted right half, search left
                if t < n[m] or t > n[r]:
                    r = m - 1

                # Target is inside the sorted right half, search right
                else:
                    l = m + 1
        
        # Target not found
        return -1

# Time Complexity: O(log N)
# Space Complexity: O(1)