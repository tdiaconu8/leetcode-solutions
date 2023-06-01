# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(node, right, curLen):
            if not node:
                return
            nonlocal res
            res = max(res, curLen)
            if right:
                dfs(node.right, False, curLen+1)
                dfs(node.left, True, 1)
            if not right:
                dfs(node.left, True, curLen+1)
                dfs(node.right, False, 1)
        
        dfs(root, True, 0)
        dfs(root, False, 0)
        return res
