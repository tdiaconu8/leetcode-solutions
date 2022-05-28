# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    
    ans = TreeNode()
    
    def dfs(n1, n2):
        if not n1:
            if not n2: return None
            if n2: return n2
        if not n2:
            if n1: return n1
        ans = TreeNode(n1.val + n2.val)
        ans.left = dfs(n1.left, n2.left)
        ans.right = dfs(n1.right, n2.right)
        return ans
        
    return dfs(root1, root2)

'''
Time : O(n)
Space : O(n)
'''