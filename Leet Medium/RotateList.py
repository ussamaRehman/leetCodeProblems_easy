from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Problem:
        Given the head of a linked list, rotate the list to the right by k places.

        Approach:
        - Count the length of the list.
        - Use k % length to skip unnecessary rotations.
        - Connect the tail to the head to make the list circular.
        - Find the new tail (at length - k steps from the head).
        - Break the circle and return the new head.

        Solution Steps:
        1. If the list is empty or has one node, return as is.
        2. Traverse the list to count length and find the tail.
        3. Adjust k with k % length.
        4. Make the list circular by linking tail.next = head.
        5. Find the new tail by moving (length - k - 1) steps from head.
        6. Break the link after the new tail and return the new head.

        Complexity:
        - Time: O(n), single traversal for length + traversal for new head.
        - Space: O(1), uses only pointers.
        """
        if not head or not head.next:
            return head

        # Step 1: Calculate the length and get the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Normalize k to avoid extra rotations
        k = k % length
        if k == 0:
            return head

        # Step 3: Make the list circular
        tail.next = head

        # Step 4: Find the new tail (length - k steps from head)
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # Step 5: Break the circle and set new head
        new_head = new_tail.next
        new_tail.next = None

        return new_head
