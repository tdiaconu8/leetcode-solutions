# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        if not root: return ''
        
        self.res = ''
        
        def preorder(node):
            if not node:
                return
            self.res += '('
            self.res += str(node.val)
            if not node.left and node.right:
                self.res += '()'
            preorder(node.left)
            preorder(node.right)
            self.res += ')'
        
        preorder(root)
        return self.res[1:-1]