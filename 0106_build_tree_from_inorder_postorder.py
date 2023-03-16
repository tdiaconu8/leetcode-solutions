# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder:
                return None
        
        val, idx = postorder[-1], inorder.index(postorder[-1])
        res = TreeNode(val)
        postorder.pop()
        res.left = self.buildTree(inorder[:inorder.index(val)], postorder[:idx])
        res.right = self.buildTree(inorder[inorder.index(val)+1:], postorder[idx:])
        
        return res

        # T: O(n^2)
        # S: O(1)
