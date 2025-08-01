# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Problem:
        Given the roots of two binary trees p and q, return True if they are identical 
        (same structure and same values), otherwise return False.

        Approach:
        - Use recursion (DFS).
        - Base Case 1: If both nodes are None, return True.
        - Base Case 2: If one is None or values differ, return False.
        - Recursive Step: Check if left subtrees AND right subtrees are identical.

        Time Complexity: O(n) – visit every node once.
        Space Complexity: O(h) – recursion stack, h = height of tree (O(log n) for balanced, O(n) worst case).
        """
        # Base case: both are None → identical here
        if not p and not q:
            return True
        
        # If one node is None or values are different → not identical
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)