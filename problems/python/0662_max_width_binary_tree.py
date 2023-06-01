from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        # BFS
        queue = deque([(root, 1)])

        while queue:
            res = max(res, queue[-1][1]-queue[0][-1]+1)
            nextLevel = deque([])
            while queue:
                node, index = queue.popleft()
                if node.left:
                    nextLevel.append((node.left, 2*index))
                if node.right:
                    nextLevel.append((node.right, 2*index+1))
            queue, nextLevel = nextLevel, deque([])

        return res

        # T: O(n)
        # S: O(n)
