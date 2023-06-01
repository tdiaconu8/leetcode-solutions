# Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

# A subtree of a node node is node plus every node that is a descendant of node.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node and node.val == 0 and not node.left and not node.right:
                return None
            return node
        
        return dfs(root)