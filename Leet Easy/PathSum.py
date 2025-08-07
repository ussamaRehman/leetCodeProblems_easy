"""
Problem:
Given the root of a binary tree and an integer targetSum,
return True if there exists a root-to-leaf path such that
the sum of the node values equals targetSum.

Approach:
- Use recursive DFS.
- At each node, subtract its value from the targetSum.
- If a leaf is reached and the remaining target is 0 → return True.
- Recurse into left and right subtrees otherwise.

Complexity:
- Time: O(n), where n is the number of nodes.
- Space: O(h), where h is the height of the tree (recursion depth).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # Check if it's a leaf node
        if not root.left and not root.right:
            return root.val == targetSum

        # Recurse into left and right with updated target
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))