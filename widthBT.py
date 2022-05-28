from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    
    if not root: return 0
    
    cur_Level = deque()
    next_Level = deque()
    cur_Level.append((root, 1))
    width = 1
    
    while cur_Level:
        width = max(width, cur_Level[-1][1] - cur_Level[0][1]+1)
        for elem in cur_Level:
            node, index = elem[0], elem[1]
            if node.left:
                next_Level.append((node.left, 2*index))
            if node.right:
                next_Level.append((node.right, 2*index+1))
        cur_Level = next_Level
        next_Level = deque()
    
    return width

'''
Time: O(n)
Space: O(n) 
'''