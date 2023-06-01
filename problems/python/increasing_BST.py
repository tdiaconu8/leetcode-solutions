# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasingBST(self, root: TreeNode) -> TreeNode:
    
    if not root: return None
    
    nodes = []
    
    def inorder(node):
        if not node: return
        inorder(node.left)
        nodes.append(node.val)
        inorder(node.right)
    
    inorder(root)
    res = TreeNode()
    
    def build(node, L, i):
        if i >= len(L): return None
        node = TreeNode(L[i])
        node.right = build(node.right, L, i+1)
        return node
    
    return build(res, nodes, 0)

'''
Time : O(n)
Space : O(n)
'''