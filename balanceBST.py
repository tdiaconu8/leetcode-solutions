# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balanceBST(self, root: TreeNode) -> TreeNode:
    
    # find all nodes in order
    self.nodes = []
    def dfs(node):
        if not node: return
        dfs(node.left)
        self.nodes.append(node.val)
        dfs(node.right)
    
    dfs(root)
    
    # Balance
    def balance(L):
        if len(L) == 0: return
        m = len(L)//2
        node = TreeNode(L[m])
        node.left = balance(L[:m])
        node.right = balance(L[m+1:])
        return node
        
    return balance(self.nodes)

    '''
    Time: O(n)
    Space: O(n)
    '''