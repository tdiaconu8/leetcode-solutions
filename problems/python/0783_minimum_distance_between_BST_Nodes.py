# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        # DFS
        def dfs(node, parentsVal):
            if not node:
                return
            for val in parentsVal:
                diff = abs(node.val - val)
                nonlocal res
                if diff < res:
                    res = diff
            parentsVal.append(node.val)
            dfs(node.left, parentsVal)
            dfs(node.right, parentsVal)
        
        res = float('inf')
        dfs(root, [])
        return res

        # n: nb of nodes
        # T: O(n)
        # S: O(1)
