class Solution:
    def integerBreak(self, n: int) -> int:
        
        # Initialize dp array where dp[i] will store the maximum product for integer i.
        dp = [0] * (n + 1)
        
        # Base case: For integer 1, the maximum product is defined as 1.
        dp[1] = 1
        
        # Loop through integers from 2 to n.
        for i in range(2, n + 1):
            
            # Set initial value for dp[i] as negative infinity to ensure any computed product is larger.
            dp[i] = -float('inf')
            
            # Try breaking the integer i into two parts: j and (i - j)
            for j in range(1, i):
                
                # Update dp[i] with the maximum product by considering:
                # 1. Breaking i into j and (i - j) without further splitting (j * (i - j))
                # 2. Breaking i into j and further splitting (i - j) (j * dp[i - j])
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        
        # Return the maximum product obtainable for integer n.
        return dp[n]

# Time Complexity: O(N^2)
# Space Complexity: O(N)
