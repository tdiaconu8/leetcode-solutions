# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    
    while root:
        if root.val < val:
            root = root.right
        elif root.val > val:
            root = root.left
        elif root.val == val:
            return root
    
    return root

'''
Time : O(h) h is the height of the tree
Space : O(0)
'''