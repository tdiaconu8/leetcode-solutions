from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return 0
        
        res = 0
        if low <= root.val <= high:
            res += root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) 
        elif root.val < low:
            res += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            res += self.rangeSumBST(root.left, low, high)
            
        return res

'''
T: O(n)
S: O(1)
'''