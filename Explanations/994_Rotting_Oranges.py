from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Get the number of rows in the grid.
        rows = len(grid)
        
        # If the grid is empty, return -1.
        if rows == 0:
            return -1
        
        # Get the number of columns in the grid.
        cols = len(grid[0])
        
        # Initialize a counter for fresh oranges.
        fresh_count = 0
        
        # Initialize a deque to hold the positions of rotten oranges.
        rotten = deque()
        
        # Iterate over every cell in the grid.
        for r in range(rows):
            for c in range(cols):
                
                # If the orange is rotten, add its position to the deque.
                if grid[r][c] == 2:
                    rotten.append((r, c))
                
                # If the orange is fresh, increment the fresh orange counter.
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # Initialize the minutes passed counter.
        minutes_passed = 0
        
        # Process the grid until no rotten oranges remain or all fresh oranges have rotted.
        while rotten and fresh_count > 0:
            
            # Increment the time (each loop level represents one minute).
            minutes_passed += 1
            
            # Process all rotten oranges in the current minute.
            for _ in range(len(rotten)):
                
                # Remove the leftmost rotten orange from the deque.
                x, y = rotten.popleft()
                
                # Check all four possible adjacent directions.
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    
                    # Compute the new coordinates.
                    xx, yy = x + dx, y + dy
                    
                    # If the new coordinates are out of grid bounds, skip to next direction.
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    
                    # If the cell is empty or already rotten, skip to next direction.
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue                        
                    
                    # A fresh orange is found; decrement the fresh counter.
                    fresh_count -= 1
                    
                    # Mark the fresh orange as rotten.
                    grid[xx][yy] = 2
                    
                    # Add the new rotten orange's position to the deque.
                    rotten.append((xx, yy))

        # Return the total minutes passed if all fresh oranges are rotten; otherwise, return -1.
        return minutes_passed if fresh_count == 0 else -1

# Time Complexity: O(rows * cols)
# Space Complexity: O(rows * cols)