from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        # T: O(n)
        # S: O(n)

        res, maxSum = 0, -10**7

        nodes, curLevel = deque([root]), 1

        while nodes:
            curSum = 0
            nextNodes = deque()
            while nodes:
                node = nodes.popleft()
                curSum += node.val
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            if curSum > maxSum:
                res, maxSum = curLevel, curSum
            curLevel += 1
            nodes, nextNodes = nextNodes, []
        
        return res