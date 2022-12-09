from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def helper(node, ancestors):
            if not node:
                return
            if not node.left and not node.right:
                if len(ancestors) < 1:
                    return
                ancestors.append(node.val)
                self.res = max(self.res, abs(max(ancestors) - min(ancestors)))
                return
            helper(node.left, ancestors + [node.val])
            helper(node.right, ancestors + [node.val])
        
        helper(root, [])
        return self.res