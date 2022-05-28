# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


def verticalTraversal(root: Optional[TreeNode]) -> List[List[int]]:
    
    coord, ans = [], []
    
    def dfs(node,r,c):
        if not node:
            return
        coord.append([c, r, node.val])
        dfs(node.left, r+1, c-1)
        dfs(node.right, r+1, c+1)
    
    dfs(root,0,0)
    coord.sort()
    
    cur_Col, cur_Trav = coord[0][0], []
    for node in coord:
        c, v = node[0], node[2]
        if c == cur_Col:
            cur_Trav.append(v)
        else:
            ans.append(cur_Trav)
            cur_Col, cur_Trav = c, []
            cur_Trav.append(v)
    if len(cur_Trav) > 0:
        ans.append(cur_Trav)
    return ans

'''
Time: O(nlogn)  --> sort operation
Space: O(n)
'''