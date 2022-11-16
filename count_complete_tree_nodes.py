from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def inorder(node):
            if not node:
                return
            self.res += 1
            inorder(node.left)
            inorder(node.right)
        
        inorder(root)
        return self.res