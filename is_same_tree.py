# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
    if not p or not q: return p == q
    
    def dfs(p, q):
        if not p and not q:
            return True
        elif p and not q or q and not p or p.val != q.val:
            return False
        return dfs(p.left, q.left) and dfs(p.right, q.right)
    
    return dfs(p,q)

    '''
    T:O(p+q)
    S: O(1)
    '''
    