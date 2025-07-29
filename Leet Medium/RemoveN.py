"""
Problem:
Given the head of a singly linked list and an integer n, remove the nth node from the end of the list 
and return its head.

Approach:
- Use a dummy node pointing to head to simplify edge cases (e.g., when removing the head itself).
- Initialize two pointers, `fast` and `slow`, at the dummy node.
- Move `fast` pointer n+1 steps ahead to create a gap of n nodes between `fast` and `slow`.
- Move both pointers together until `fast` reaches the end.
- `slow` will now be just before the node that needs to be removed.
- Adjust `slow.next` to skip the target node.

Solution Steps:
1. Create a dummy node pointing to head.
2. Move `fast` n+1 steps ahead.
3. Move both `fast` and `slow` pointers together until `fast` reaches the end.
4. Remove the nth node by skipping it (`slow.next = slow.next.next`).
5. Return `dummy.next` as the new head.

Complexity:
- Time Complexity: O(L), where L is the number of nodes (single traversal).
- Space Complexity: O(1), only uses two pointers regardless of input size.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Step 1: Dummy node to handle edge cases cleanly (like deleting the head)
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        # Step 2: Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Step 3: Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Step 4: Remove nth node from the end
        slow.next = slow.next.next

        # Step 5: Return new head (dummy.next handles case where head was removed)
        return dummy.next