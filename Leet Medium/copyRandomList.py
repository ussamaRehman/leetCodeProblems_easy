"""
Problem:
Given a linked list where each node has a 'next' and 'random' pointer,
create a deep copy of the list.

Approach (O(1) space):
Clone each node and insert it right after the original.
Assign random pointers for the cloned nodes.
Detach cloned list from the original list.

Complexity:
- Time: O(n) → Three passes through the list.
- Space: O(1) → No extra data structure, only the cloned nodes.
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return None

        # --- Step 1: Interweave cloned nodes ---
        current = head
        while current:
            new_node = Node(current.val)   # clone the node
            new_node.next = current.next   # link clone to next
            current.next = new_node        # insert clone after original
            current = new_node.next        # move to the next original

        # --- Step 2: Assign random pointers ---
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next    # skip clones to only visit originals

        # --- Step 3: Detach cloned list ---
        current = head
        copy_head = head.next
        while current:
            clone = current.next
            current.next = clone.next      # restore original 'next'
            current = current.next
            if current:
                clone.next = current.next  # link clone to next clone

        return copy_head