from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            self.nodes.append(node.val)
            inorder(node.right)
        inorder(root)
        self.p = -1

    def next(self) -> int:
        self.p += 1
        return self.nodes[self.p]

    def hasNext(self) -> bool:
        return True if self.p+1 < len(self.nodes) else False
    