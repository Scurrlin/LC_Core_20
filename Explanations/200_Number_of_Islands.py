class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Edge case: Empty grid
        if not grid:
            return 0
        
        def dfs(i, j):

            # Out-of-bounds or water('0') check
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            
            # Mark as visited
            grid[i][j] = '0'

            # Explore all 4 directions
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # Counter for number of islands
        num_islands = 0

        # Iterate through the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # Found a new island
                if grid[i][j] == '1':
                    num_islands += 1

                    # Perform DFS to mark entire island
                    dfs(i, j)
        
        # Return total count of islands
        return num_islands

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)