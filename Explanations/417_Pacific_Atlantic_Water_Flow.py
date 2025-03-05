class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        # Track reachable cells for each ocean
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):

            # Stop DFS if out of bounds, already visited, or height decreases
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            
            # Mark as visited
            visit.add((r, c))

            # Explore all four directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Start DFS from the first and last row (Pacific & Atlantic borders)
        for c in range(COLS):

            # Pacific (Top row)
            dfs(0, c, pac, heights[0][c])

            # Atlantic (Bottom row)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # Start DFS from the first and last column (Pacific & Atlantic borders)
        for r in range(ROWS):

            # Pacific (Left column)
            dfs(r, 0, pac, heights[r][0])

            # Atlantic (Right column)
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # Find all coordinates that can reach both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

# Time Complexity: O(M x N)
# Space Complexity: O(M x N)