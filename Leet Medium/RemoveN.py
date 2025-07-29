# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases like removing the head
        dummy = ListNode(0)
        dummy.next = head

        # First pass: find the length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Second pass: stop right before the node we want to remove
        current = dummy
        for _ in range(length - n):
            current = current.next

        # Remove the target node
        current.next = current.next.next

        return dummy.next
