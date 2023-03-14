# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(node, curNum):
            if not node.left and not node.right:
                nonlocal res
                res += curNum*10+node.val
                return
            if node.left:
                dfs(node.left, curNum*10+node.val)
            if node.right:
                dfs(node.right, curNum*10+node.val)
        
        dfs(root, 0)
        return res

        # T: O(n)
        # S: O(1)
