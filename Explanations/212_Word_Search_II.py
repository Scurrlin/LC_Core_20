class TrieNode:

    # Initialize a new TrieNode.
    def __init__(self):
        
        # Dictionary to store child nodes for each character.
        self.children = {}
        
        # Boolean flag to indicate if this node represents the end of a word.
        self.isWord = False
        
        # Reference count to track how many words pass through this node.
        self.refs = 0

    # Add a word to the Trie.
    def addWord(self, word):
        
        # Start from the current node (root).
        cur = self
        
        # Increment reference count for the current node.
        cur.refs += 1
        
        # Iterate over each character in the word.
        for c in word:
            
            # If the character is not a child, create a new TrieNode.
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            # Move to the child node corresponding to the character.
            cur = cur.children[c]
            
            # Increment reference count for the child node.
            cur.refs += 1
        
        # Mark the end node as representing a complete word.
        cur.isWord = True

    # Remove a word from the Trie.
    def removeWord(self, word):
        
        # Start from the current node (root).
        cur = self
        
        # Decrement reference count for the current node.
        cur.refs -= 1
        
        # Iterate over each character in the word.
        for c in word:
            
            # If the character exists among the children.
            if c in cur.children:
                
                # Move to the child node corresponding to the character.
                cur = cur.children[c]
                
                # Decrement reference count for the child node.
                cur.refs -= 1

# Time Complexity: O(L)
# Space Complexity: O(1)