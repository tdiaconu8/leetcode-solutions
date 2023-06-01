from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                while queue:
                    remNode = queue.popleft()
                    if not remNode:
                        continue
                    return False
            elif node:
                queue.append(node.left)
                queue.append(node.right)
        
        return True

        # T: O(n)
        # S: O(n)
