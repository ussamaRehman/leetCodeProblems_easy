from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Problem:
        Check if a binary tree is symmetric around its center.

        Approach:
        - Use recursion to check if left and right subtrees are mirror images.
        - isMirror(t1, t2):
            - If both None → True
            - If one None → False
            - Check if:
                - t1.val == t2.val
                - t1.left mirrors t2.right
                - t1.right mirrors t2.left
        """

        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and
                    isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))

        return isMirror(root.left, root.right) if root else True