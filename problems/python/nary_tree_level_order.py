# Definition for a Node.
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root: return []
        
        res = []
        queue = deque([])
        queue.append(root)
        
        while queue:
            tmp, cur = deque([]), []
            while queue:
                node = queue.popleft()
                cur.append(node.val)
                if node.children:
                    for child in node.children:
                        tmp.append(child)
            res.append(cur)
            queue = tmp
            tmp, cur = deque([]), []
        
        return res