
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        count = 1
        if root.left:
            count = preorder(root.left, count)
        if root.right:
            count = preorder(root.right, count)

        def preorder(root, count):
            count += 1
            if root.left:
                count = preorder(root.left, count)

            if root.right:
                count = preorder(root.right, count)
