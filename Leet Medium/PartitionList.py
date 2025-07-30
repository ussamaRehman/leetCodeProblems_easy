from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Problem:
        Given the head of a linked list and a value x, partition it so that all nodes less than x 
        come before nodes greater than or equal to x. Preserve the original relative order of nodes 
        in each partition.

        Approach:
        - Use two dummy nodes to simplify building two lists:
            1. `before_head` for nodes < x.
            2. `after_head` for nodes >= x.
        - Traverse the original list once, attaching each node to the correct list.
        - Connect the end of the `before` list to the start of the `after` list.
        - Ensure `after` list is terminated with None to avoid cycles.

        Complexity:
        - Time: O(n) — Single traversal of the list.
        - Space: O(1) — Only uses dummy nodes and pointers, no extra structures.
        """

        before_head = before = ListNode(0)   # Dummy head for < x
        after_head = after = ListNode(0)     # Dummy head for >= x

        # Traverse the list and partition into before/after lists
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        # Important: terminate after list to avoid cycle
        after.next = None
        # Connect before list to after list
        before.next = after_head.next

        return before_head.next