class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Get the length of the input string s.
        n = len(s)
        
        # Initialize dp array of length n+1 where dp[i] indicates if s[:i] can be segmented.
        dp = [False] * (n + 1)
        
        # Base case: an empty string can always be segmented.
        dp[0] = True
        
        # Compute the maximum length of words in the dictionary to limit the inner loop.
        max_len = max(map(len, wordDict))

        # Iterate over each index from 1 to n (end position of the substring).
        for i in range(1, n + 1):
            
            # Check potential partition points for the substring ending at i,
            # starting from i-1 down to max(i - max_len, 0) to only consider relevant word lengths.
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                
                # If s[:j] can be segmented and s[j:i] is in the word dictionary,
                # then s[:i] can also be segmented.
                if dp[j] and s[j:i] in wordDict:
                    
                    # Mark dp[i] as True since a valid segmentation for s[:i] is found.
                    dp[i] = True
                    
                    # No need to check further partitions for s[:i].
                    break
        
        # Return whether the entire string s can be segmented.
        return dp[n]

# Time Complexity: O(N * max_len)
# Space Complexity: O(N)