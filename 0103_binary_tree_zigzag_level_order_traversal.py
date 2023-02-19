from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return None
        
        # BFS
        res = []
        queue = deque([root])
        left = True

        while queue:
            nextLevel, curLevel = deque([]), []
            while queue:
                node = queue.popleft()
                curLevel.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            queue = nextLevel
            if not left:
                curLevel = curLevel[::-1]
            res.append(curLevel)
            left = not left
        
        return res

        # T: O(n)
        # S: O(n)
