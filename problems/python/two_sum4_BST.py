from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        vals = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        
        inorder(root)
        if len(vals) < 2:
            return False
        
        lookup = {}
        for val in vals:
            if k-val in lookup:
                return True
            lookup[val] = 1
        
        return False
