# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        # T: O(2**n)
        # S: O(n)

        res = []

        if n % 2 == 0:
            return res
        
        if n == 1:
            return [TreeNode()]
        
        for i in range(1, n-1, 2):
            left, right = self.allPossibleFBT(i), self.allPossibleFBT(n-1-i)
            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    res.append(root)
        
        return res        