class Solution:
  def minDistance(self, word1: str, word2: str) -> int:

    # Get the length of word1
    m = len(word1)
    
    # Get the length of word2
    n = len(word2)

    # Initialize a DP table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill first column: converting word1[0:i] to empty string requires i deletions
    for i in range(1, m + 1):
      dp[i][0] = i

    # Fill first row: converting empty string to word2[0:j] requires j insertions
    for j in range(1, n + 1):
      dp[0][j] = j

    # Compute the DP table values
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
          
          # Characters match; no operation needed, so copy the previous value
          dp[i][j] = dp[i - 1][j - 1]
        else:
          
          # Characters don't match; take the min of replace, delete, or insert, then add 1 operation
          dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    # Return the edit distance between word1 and word2
    return dp[m][n]

# Time Complexity: O(M * N)
# Space Complexity: O(M * N)