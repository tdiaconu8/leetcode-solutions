# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    
    nodes = []
    
    if not root: return []
    
    def dfs(node):
        if not node: return
        dfs(node.left)
        dfs(node.right)
        nodes.append(node.val)
        return nodes
    
    return dfs(root)

'''
Time : O(n)
Space : O(n)
'''