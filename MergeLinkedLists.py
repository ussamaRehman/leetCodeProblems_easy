"""
Problem: Merge Two Sorted Lists.
Given two sorted linked lists (list1 and list2), merge them into a single sorted linked list 
and return its head.

Approach:
- Use a dummy node to simplify edge cases (e.g., starting the merged list).
- Maintain a 'tail' pointer to build the new list.
- Traverse both lists, comparing nodes:
    * Attach the smaller node to 'tail'.
    * Move the pointer forward in the list from which the node was taken.
- After one list ends, attach the remaining nodes of the other list.

Solution:
- Initialize a dummy ListNode and a tail pointer.
- Iterate while both lists have nodes, always attaching the smaller node.
- Attach the leftover nodes (if any) after the loop.
- Return dummy.next (skipping the placeholder node).

Complexity:
- Time: O(n + m), where n and m are the lengths of list1 and list2.
- Space: O(1), since we reuse existing nodes and only create one dummy node.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node to simplify operations at head
        dummy = ListNode()
        tail = dummy  # Tail will track the end of the merged list

        # Merge the lists while both have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Move tail forward

        # Attach any remaining nodes from either list1 or list2
        tail.next = list1 if list1 else list2

        # Return the head of the merged list (skip dummy node)
        return dummy.next