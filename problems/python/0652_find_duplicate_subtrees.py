from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        res, nodesMap = [], defaultdict(int)
        
        # Get inorder of the current node root
        def getInorder(node):
            if not node:
                return ''
            inorder = '(' + getInorder(node.left) + str(node.val) + getInorder(node.right) + ')'
            nodesMap[inorder] += 1
            if nodesMap[inorder] == 2:
                nonlocal res
                res.append(node)
            return inorder

        getInorder(root)
        
        return res

        # T: O(n)
        # S: O(n)
