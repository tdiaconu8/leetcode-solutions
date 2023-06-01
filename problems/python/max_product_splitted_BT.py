from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        MOD = 10**9 + 7
        self.totalSum = 0
        self.res = 0

        def totalSum(node):
            if not node:
                return 0
            res = node.val
            res += totalSum(node.left) + totalSum(node.right)
            return res
        
        self.totalSum = totalSum(root)

        def dfs(node):
            if not node:
                return 0
            node.val += dfs(node.left) + dfs(node.right)
            self.res = max(self.res, node.val * (self.totalSum - node.val))
            return node.val
        
        dfs(root)
        return self.res % MOD