"""
Problem:
Populate each node's next pointer to its next right node in a binary tree.
If there is no next right node, the next pointer should be set to None.
The tree is not necessarily perfect or complete.

Approach:
- Use three pointers:
  * curr: current node on the current level
  * prev: previous node on the next level, used to link next pointers
  * head: head of the next level
- Traverse current level using curr and existing next pointers.
- While traversing, build next pointers for the next level.
- Move curr to head to proceed to the next level.
- Repeat until no more levels.

Complexity:
- Time: O(n), each node visited once.
- Space: O(1), constant extra space.
"""

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root

        while curr:
            head = None  # head of next level
            prev = None  # previous node on next level

            while curr:
                for child in [curr.left, curr.right]:
                    if child:
                        if prev:
                            prev.next = child
                        else:
                            head = child
                        prev = child
                curr = curr.next

            curr = head

        return root