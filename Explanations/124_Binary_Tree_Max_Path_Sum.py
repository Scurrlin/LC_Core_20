class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        # Initialize result with the root's value in a list for mutable access in nested function.
        res = [root.val]

        # Define a recursive DFS function to calculate maximum path sum from each node.
        def dfs(root):
            
            # If the current node is None, return 0 (base case).
            if not root:
                return 0

            # Recursively compute maximum path sum from the left subtree.
            leftMax = dfs(root.left)
            
            # Recursively compute maximum path sum from the right subtree.
            rightMax = dfs(root.right)
            
            # Only consider positive contributions from the left subtree.
            leftMax = max(leftMax, 0)
            
            # Only consider positive contributions from the right subtree.
            rightMax = max(rightMax, 0)
            
            # Update the global maximum path sum by considering the path through the current node.
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # Return the maximum path sum that can be extended to the current node's parent.
            return root.val + max(leftMax, rightMax)

        # Start the DFS traversal from the root.
        dfs(root)
        
        # Return the maximum path sum found.
        return res[0]

# Time Complexity: O(N)
# Space Complexity: O(N)