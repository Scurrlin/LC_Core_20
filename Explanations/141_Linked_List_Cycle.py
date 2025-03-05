class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Initialize slow and fast pointers
        slow, fast = head, head

        # Ensure fast pointer doesn't hit None
        while fast and fast.next:

            # Move slow pointer one step
            slow = slow.next

            # Move fast pointer two steps
            fast = fast.next.next

            # If they meet, a cycle exists
            if slow == fast:
                return True
            
        # If we exit the loop, no cycle exists
        return False

# Time Compexity: O(N)
# Space Complexity: O(1)