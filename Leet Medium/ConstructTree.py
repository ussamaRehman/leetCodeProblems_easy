"""
Problem:
Given preorder and inorder traversal of a binary tree, construct the tree.

Approach:
- Use preorder to pick the root.
- Use inorder to find left/right subtree boundaries.
- Recursively build left and right subtrees.

Complexity:
- Time: O(n) because each node is visited once.
- Space: O(n) for recursion stack and hashmap.
"""

class Solution:
    def buildTree(self, preorder, inorder):
        # Build a hashmap for inorder values to indices
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0  # pointer for preorder

        def array_to_tree(left, right):
            # if there are no elements in this subtree
            if left > right:
                return None

            # Pick current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            # Create root node
            root = TreeNode(root_val)   # ✅ Use LeetCode's TreeNode class

            # Build left and right subtrees
            idx = inorder_map[root_val]
            root.left = array_to_tree(left, idx - 1)
            root.right = array_to_tree(idx + 1, right)

            return root

        # Start with the full range of inorder
        return array_to_tree(0, len(inorder) - 1)