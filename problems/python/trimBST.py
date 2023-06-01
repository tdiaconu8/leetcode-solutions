# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


def trimBST(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    
    def dfs(node):
        if not node:
            return None
        node.left = dfs(node.left)
        node.right = dfs(node.right)
        if high < node.val:
            return node.left
        if low > node.val:
            return node.right
        else:
            return node
    
    
    return dfs(root)
    
    '''
    Time : O(n)
    Space : O(0)
    '''