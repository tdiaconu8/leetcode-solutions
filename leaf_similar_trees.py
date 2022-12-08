from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def find_seq(node):
            res = []
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            res += find_seq(node.left) + find_seq(node.right)
            return res
            
        return find_seq(root1) == find_seq(root2)