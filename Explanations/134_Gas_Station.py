class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # If total gas is less than total cost, return -1
        if sum(gas) < sum(cost):
            return -1
        
        # Initialize starting point and fuel tank
        start, tank = 0, 0

        # Iterate through each station
        for i in range(len(gas)):

            # Update gas in tank after traveling to station
            tank += gas[i] - cost[i]

            # If tank is negative, can't continue from current start
            if tank < 0:

                # Move the starting station forward
                start = i + 1

                # Reset the tank
                tank = 0

        # Return the starting station        
        return start

# Time Compexity: O(N)
# Space Complexity: O(1)