from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def dfs(node, curDepth, leftFlag):
            if not node:
                return None
            if depth == 1:
                return TreeNode(val, node, None)
            elif curDepth == depth-1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
            node.left = dfs(node.left, curDepth + 1, True)
            node.right = dfs(node.right, curDepth + 1, False)
            return node
        
        return dfs(root, 1, True)