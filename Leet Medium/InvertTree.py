# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Problem:
        Given the root of a binary tree, invert the tree and return its root.

        Approach:
        - Recursively swap left and right children for every node (DFS).
        - Base Case: if node is None, return None.
        - Recursive Case: invert left, invert right, then swap.

        Time Complexity: O(n) – every node visited once.
        Space Complexity: O(h) – recursion stack (h = tree height).
        """
        if not root:
            return None
        
        # Swap children
        root.left, root.right = root.right, root.left

        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root