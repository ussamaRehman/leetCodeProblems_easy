"""
Problem:
Given the root of a binary tree, flatten the tree into a "linked list" in-place.
- The linked list should use the same TreeNode structure, where the right child pointer points to the next node in preorder traversal.
- The left child pointer should always be None.

Approach (Iterative / Morris Traversal-like):
1. Start at the root node.
2. For each node:
   - If there is a left subtree:
       a. Find the rightmost node in the left subtree.
       b. Link that node's right pointer to the current node's right subtree.
       c. Move the left subtree to the right.
       d. Set left pointer to None.
   - Move to the next node in the right.
3. Continue until all nodes are processed.

Why Efficient:
- No recursion → no extra call stack.
- No extra data structures → works in-place.

Complexity:
- Time Complexity: O(n), where n is the number of nodes (each node visited at most twice).
- Space Complexity: O(1), in-place.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        current = root
        
        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Connect right subtree to rightmost node's right
                rightmost.right = current.right
                
                # Move left subtree to right
                current.right = current.left
                current.left = None
            
            # Move to next right node
            current = current.right