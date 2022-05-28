# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    def dfs(node, curSum):
        if not node: return curSum
        curSum = dfs(node.right, curSum)
        curSum += node.val
        node.val = curSum
        curSum = dfs(node.left, curSum)
        return curSum
    
    dfs(root, 0)
    return root

    '''
    Time : O(n)
    Space : O(1)
    '''

    '''
    FIRST APPROACH
    if not root: return None
    # find all nodes values
    node, values = root, []
    def dfs(node):
        if not node: return
        values.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    
    # for each node add greater values
    def addGreater(val, L):
        s = val
        for num in L:
            if num > val: s+= num
        return s
    
    def dfs2(node):
        if not node: return
        node.val = addGreater(node.val, values)
        dfs2(node.left)
        dfs2(node.right)
    dfs2(root)
    return root
    '''

    '''
    Time : O(n*n)
    Space : O(n)
    '''