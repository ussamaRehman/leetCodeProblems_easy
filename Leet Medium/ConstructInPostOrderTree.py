"""
Problem:
Given inorder and postorder traversal of a binary tree,
construct and return the binary tree.

Approach:
- The last element in postorder is the root of the current subtree.
- Use a hashmap to find root index in inorder for quick splits.
- Recursively build right subtree first, then left subtree.
- Use a pointer to track current root index in postorder, moving backward.

Complexity:
- Time: O(n), each node is visited once.
- Space: O(n) for recursion stack and hashmap.
"""

from typing import Optional, List

# Definition for a binary tree node.
# Note: On LeetCode, TreeNode is pre-defined, so no need to redefine.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            idx = inorder_map[root_val]

            # Important: build right subtree first
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)

            return root

        return helper(0, len(inorder) - 1)