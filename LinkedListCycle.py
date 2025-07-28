"""
Problem:
    Linked List Cycle
    Given the head of a singly linked list, determine if the linked list contains a cycle.

Approach:
    Traverse the linked list while keeping track of visited nodes using a set.
    If a node is revisited, a cycle exists. Otherwise, if the end is reached, there is no cycle.

Solution:
    Iterate through the linked list, adding each node to a set.
    If a node is already in the set, return True (cycle detected).
    If the end of the list is reached (current is None), return False (no cycle).

Complexity:
    Time Complexity: O(n), where n is the number of nodes in the list.
    Space Complexity: O(n), due to the extra space used by the set to store visited nodes.
"""
from typing import Optional

#
# Definition for singly-linked list node.
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hasCycle checks for cycles by tracking visited nodes in a set
        current = head
        if not current:
            return False
        
        seen = set()
        while current:
            # If current node is already seen, a cycle exists
            if current in seen:
                return True
            else:
                # Add current node to the set and move to the next node
                seen.add(current)
                current = current.next
        # No cycle found after traversing the list
        return False