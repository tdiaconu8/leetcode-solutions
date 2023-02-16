# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # DFS
        def dfs(node, curDepth):
            if not node:
                return
            if not node.left and not node.right: # it is a leaf node
                nonlocal res
                res = max(res, curDepth)
                return
            if node.left:
                dfs(node.left, curDepth+1)
            if node.right:
                dfs(node.right, curDepth+1)

        res = 0
        dfs(root, 1)
        return res
      
      # n: number of nodes
      # T: O(n)
      # S: O(1)
