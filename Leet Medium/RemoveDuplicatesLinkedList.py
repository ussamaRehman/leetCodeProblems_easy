from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem:
        Given a sorted linked list, delete all nodes that have duplicate numbers,
        leaving only distinct numbers.

        Approach (One-pass, O(1) space):
        - Use a dummy node to simplify removing the head if needed.
        - Traverse with two pointers: prev (tracks last non-duplicate node) and current.
        - When we find duplicates, skip the whole block of duplicates.
        - Continue until the end.

        Complexity:
        - Time: O(n), single traversal
        - Space: O(1), no extra data structures used
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            # If we found a duplicate block
            if current.next and current.val == current.next.val:
                dup_val = current.val
                # Skip all nodes with this value
                while current and current.val == dup_val:
                    current = current.next
                # Connect prev to the first distinct node
                prev.next = current
            else:
                prev = current
                current = current.next

        return dummy.next