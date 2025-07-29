"""
Reverse the nodes of a linked list from position left to right in-place.

Approach:
- Use a dummy node to simplify edge cases (like when left = 1).
- Traverse the list until the node before the 'left' position.
- Reverse the sublist between left and right by pointer manipulation.
- Connect the reversed sublist back to the main list.

Time Complexity: O(n) — traverse the list once
Space Complexity: O(1) — no extra data structures used
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move `prev` to the node just before `left`
        for _ in range(left - 1):
            prev = prev.next

        # `start` will become the tail of the reversed section
        start = prev.next
        then = start.next

        # Step 2: Reverse nodes between left and right
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next
