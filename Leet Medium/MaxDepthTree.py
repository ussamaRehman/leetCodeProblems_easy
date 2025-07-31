"""
Problem:
Given the root of a binary tree, return its maximum depth.
The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Approach (DFS - Recursion):
- Use recursion to compute the depth of the left and right subtrees.
- The depth of the tree at any node = 1 (for the node itself) + 
  the maximum depth of its left and right subtrees.
- Base case: if the node is None, return 0.

Complexity:
- Time: O(n), where n is the number of nodes (we visit every node once).
- Space: O(h), where h is the height of the tree (recursion stack).
"""

class Solution:
    def maxDepth(self, root):
        # Base case: if tree is empty, depth is 0
        if not root:
            return 0
        
        # Recursive case:
        # 1 for the current node + the deeper side between left & right
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))