from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
    
    def valid(node, l, r):
        if not node:
            return True
        if node.val >= r or node.val <= l:
            return False
        return valid(node.left, l, node.val) and valid(node.right, node.val, r)
    
    return valid(root, -2**31-1, 2**31)
    
    '''
    T: O(n)
    S: O(1)
    '''
    
    # Inorder: O(nlogn)
    '''
    self.nodes = []
    def inorder(node):
        if not node: return
        inorder(node.left)
        self.nodes.append(node.val)
        inorder(node.right)
    
    inorder(root)
    
    return self.nodes == sorted(self.nodes) and self.nodes == sorted(list(set(self.nodes)))

    '''
    '''
    T: O(nlogn)
    S: O(n)
    '''