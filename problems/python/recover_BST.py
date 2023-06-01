from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverTree(root: Optional[TreeNode]) -> None:
    
    nodes = []
    
    def inorder(node):
        if not node: return
        inorder(node.left)
        nodes.append(node.val)
        inorder(node.right)
    
    inorder(root)
    corr, wrong = sorted(nodes), {}
    for i, e in enumerate(nodes):
        if e != corr[i]:
            wrong[e] = corr[i] + wrong.get(e, 0)
    print(wrong)
    
    def replace(node):
        if not node: return
        if node.val in wrong.keys(): node.val = wrong[node.val]
        replace(node.left)
        replace(node.right)
    
    replace(root)
    
    '''
    T: O(nlogn)
    S: O(n)
    '''
