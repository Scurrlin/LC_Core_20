class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Set 'a' as the target amount for clarity.
        a = amount
        
        # Initialize minC list with a+1 (an impossible high value) for all amounts from 0 to a.
        minC = [a + 1] * (a + 1)
        
        # Base case: 0 coins are needed to reach amount 0.
        minC[0] = 0
        
        # Iterate over each sub-amount from 1 to a.
        for i in range(1, a + 1):
            
            # Check each coin denomination.
            for c in coins:
                
                # If the coin can be used (i.e., coin value is not greater than the sub-amount).
                if i - c >= 0:
                    
                    # Update minC[i] with the minimum coins needed using the current coin.
                    minC[i] = min(minC[i], 1 + minC[i - c])
        
        # If minC[a] is still a+1, it means the amount cannot be reached, so return -1; otherwise, return minC[a].
        return minC[-1] if minC[-1] != a + 1 else -1

# Time Complexity: O(amount * len(coins))
# Space Complexity: O(amount)