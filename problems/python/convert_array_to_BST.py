from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    
    def builder(node, L):
        if len(L) == 0:
            return None
        m = len(L)//2
        node = TreeNode(L[m])
        node.left = builder(node.left, L[:m])
        node.right = builder(node.right, L[m+1:])
        return node
    
    root = TreeNode()
    return builder(root, nums)

'''
Time: O(n)
Space: O(n)
'''